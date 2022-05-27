import asyncio
import httpx
from bs4 import BeautifulSoup
import aiofiles


async def main():
    async with httpx.AsyncClient() as client:
        url = "https://www.weather.gov/lwx/"
        url_root = "https://www.weather.gov/"
        response = await client.get(url)
        print(response)
        # print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        image = soup.find("input", {"id": "wwamapImage"})
        # print(image)
        image_photo_url = f'{url_root}{image["src"]}'
        response_get_photo = await client.get(image_photo_url)
        async with aiofiles.open("test.png", "wb") as f:
            await f.write(response_get_photo.content)


if __name__ == "__main__":
    asyncio.run(main=main())
