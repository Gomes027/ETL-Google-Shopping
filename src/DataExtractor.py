from playwright.async_api import async_playwright

class ProductExtractor:
    def __init__(self, search_query):
        self.search_query = search_query
        self.produtos = []

    async def extract(self):
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=False)
            page = await browser.new_page()

            await page.goto(f'https://www.google.com/search?q={self.search_query}&tbm=shop')

            page_number = 1

            while True:
                await page.wait_for_selector('.sh-dgr__content')

                products = await page.query_selector_all('.sh-dgr__content')
                print(f'\nExtraindo dados da página {page_number}...')

                for product in products:
                    await self.extract_product_data(product)

                next_page = await page.query_selector('td[aria-level="3"] a#pnnext')

                if next_page:
                    next_page_href = await next_page.get_attribute('href')
                    if next_page_href:
                        await page.goto(f'https://www.google.com{next_page_href}')
                        page_number += 1
                        await page.wait_for_timeout(2000)
                    else:
                        break
                else:
                    break

            await browser.close()
            return self.produtos

    async def extract_product_data(self, product):
        titulo = await product.query_selector('h3.tAxDx')
        preco = await product.query_selector('span.a8Pemb.OFFNJ')
        loja = await product.query_selector('div.aULzUe.IuHnof')
        nota_avaliacao = await product.query_selector('span.Rsc7Yb')
        qtde_avaliacao_element = await product.query_selector('xpath=//div[@class="NzUzee"]/div/span[1]')
        frete = await product.query_selector('div.vEjMR')
        imagem_element = await product.query_selector('div.ArOc1c img')
        link_element = await product.query_selector('div.mnIHsc a')

        titulo_text = await titulo.inner_text() if titulo else None
        preco_text = await preco.inner_text() if preco else None
        loja_text = await loja.inner_text() if loja else None
        nota_avaliacao_text = await nota_avaliacao.inner_text() if nota_avaliacao else None
        qtde_avaliacao_text = await qtde_avaliacao_element.inner_text() if qtde_avaliacao_element else None
        frete_text = await frete.inner_text() if frete else None
        imagem_link = await imagem_element.get_attribute('src') if imagem_element else None

        link_href = await link_element.get_attribute('href') if link_element else None
        if link_href and "/url?url=" in link_href:
            link_href = link_href.replace("/url?url=", "")

        qtde_avaliacao = qtde_avaliacao_text.split()[-1] if qtde_avaliacao_text else None

        self.produtos.append({
            'produto': titulo_text,
            'preco': preco_text,
            'loja': loja_text,
            'nota_avaliacao': nota_avaliacao_text,
            'qtde_avaliacao': qtde_avaliacao,
            'frete': frete_text,
            'imagem_link': imagem_link,
            'produto_link': link_href
        })
