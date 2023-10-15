import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


def create_profile_image(url, username, total_xp):
    level = total_xp // 60
    xp = total_xp % 60

    res = requests.get(url)
    if res.ok == 404:
        return Image.open("C:\\coding\\python\\kl\\kl_disnake_tools_bot\\public\\img\\404.jpg")
    pfp = BytesIO(res.content)


    # Circularize the user pfp
    with Image.open(pfp) as im:
        width, height = im.size
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, width, height), fill=255)
        result = Image.new("RGBA", (width, height))
        result.paste(im, mask=mask)


    # Resizing the user pfp due to my low knowledge of image manipulation
    
    new_width = 120
    new_height = 120
    result = result.resize((new_width, new_height))


    # Pasting the pfp, username, level etc.. to base image
    with Image.open("C:\\coding\\python\\kl\\kl_disnake_tools_bot\\public\\img\\ref.png") as im:
        im.paste(result, (10, 10), result)
        font = ImageFont.truetype("C:\\coding\\python\\kl\\kl_disnake_tools_bot\\public\\fonts\\Arial.ttf", 35)
        font2 = ImageFont.truetype("C:\\coding\\python\\kl\\kl_disnake_tools_bot\\public\\fonts\\Arial.ttf", 30)
        draw = ImageDraw.Draw(im)
        draw.text(xy=(145, 30), text=username, font=font, fill=(255, 255, 255, 255))
        draw.text(xy=(380,97),font=font2, text=f"{xp}/60")
        draw.text(xy=(230,97),font=font2,text=str(level))
        return im
    