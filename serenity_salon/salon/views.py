from django.http import HttpResponse

def home(request):
    html = """
    <html>
    <head><title>Serenity</title></head>
    <body style="background: #f9f7f4; font-family: sans-serif; text-align: center; padding: 50px;">
        <h1 style="color: #4a4a4a;">Гармония красоты и спокойствия</h1>
        <p style="color: #777;">Serenity — это пространство, где современные beauty-технологии сочетаются с атмосферой умиротворения.</p>
        <a href="/appointment/" style="display: inline-block; background: #a0b6b6; color: white; padding: 15px 30px; margin: 10px; text-decoration: none; border-radius: 4px;">Записаться онлайн</a>
        <a href="/services/" style="display: inline-block; border: 2px solid #4a4a4a; color: #4a4a4a; padding: 15px 30px; margin: 10px; text-decoration: none; border-radius: 4px;">Наши услуги</a>
    </body>
    </html>
    """
    return HttpResponse(html)