from flask import Flask,render_template
import test
import namess
import dice
import os
os.system('pip install flask')
app=Flask(__name__)
@app.route('/')
def start():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #e0f7fa;
            color: #333;
            overflow-x: hidden;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        h1 {
            color: #00796b;
            margin-bottom: 20px;
        }
        .button {
            display: inline-block;
            padding: 15px 25px;
            font-size: 18px;
            color: #fff;
            background-color: #00796b;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #004d40;
        }
        footer {
            margin-top: 30px;
            font-size: 14px;
            color: #00796b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>💎 Main Page 💎</h1>
        <a class="button" href="/names">Adlar Siyahisi</a>
        <a class="button" href="/zer">Zer oyunu</a>
        <footer>Flask ilə hazırlanan bir veb tətbiqi</footer>
    </div>
</body>
</html>

    '''
    

@app.route('/names')
def name():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Names</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #e0f7fa;
            color: #333;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        h1 {
            color: #00796b;
            margin-bottom: 20px;
        }
        .button {
            display: inline-block;
            padding: 15px 25px;
            font-size: 18px;
            color: #fff;
            background-color: #00796b;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            margin: 10px 5px;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #004d40;
        }
        footer {
            margin-top: 30px;
            font-size: 14px;
            color: #00796b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Adlar Siyahisi</h1>
        <a class="button" href="/fullname">Ad ve Soyad</a>
        <a class="button" href="/name">Yalniz Ad</a>
        <a class="button" href="/surname">Yalniz Soyad</a>
        <footer>Flask ilə hazırlanan bir veb tətbiqi</footer>
    </div>
</body>
</html>

    '''
@app.route('/fullname')
def fullname():
   Ad=namess.get_name()
   soyad=namess.get_surname()
   
   return  f'''
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heyata Qarsiniza Cixacaq Insan</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #e0f7fa;
            color: #333;
        }}
        .container {{
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
        }}
        h1 {{
            color: #00796b;
            margin-bottom: 20px;
        }}
        .content {{
            margin-top: 20px;
            font-size: 18px;
            color: #004d40;
        }}
        .button {{
            display: inline-block;
            padding: 15px 25px;
            font-size: 18px;
            color: #fff;
            background-color: #00796b;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            margin-top: 20px;
            transition: background-color 0.3s;
        }}
        .button:hover {{
            background-color: #004d40;
        }}
        footer {{
            margin-top: 30px;
            font-size: 14px;
            color: #00796b;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>❤ Heyata Qarsiniza Cixacaq Insan:</h1>
        <div class="content">
            <strong>{Ad} {soyad}</strong>
        </div>
        <a class="button" href="/">Ana Səhifəyə Dön</a>
        <footer>Flask ilə hazırlanan bir veb tətbiqi</footer>
    </div>
</body>
</html>
   
   '''
   
@app.route('/name')
def only_name():
    Ad=namess.get_name()
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yalnız Ad</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #e0f7fa;
                color: #333;
            }}
            .container {{
                width: 90%;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                text-align: center;
            }}
            h1 {{
                color: #00796b;
                margin-bottom: 20px;
            }}
            .content {{
                margin-top: 20px;
                font-size: 18px;
                color: #004d40;
            }}
            .button {{
                display: inline-block;
                padding: 15px 25px;
                font-size: 18px;
                color: #fff;
                background-color: #00796b;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin-top: 20px;
                transition: background-color 0.3s;
            }}
            .button:hover {{
                background-color: #004d40;
            }}
            footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #00796b;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Yalnız Ad:</h1>
            <div class="content">
                <strong>{Ad}</strong>
            </div>
            <a class="button" href="/">Ana Səhifəyə Dön</a>
            <footer>Flask ilə hazırlanan bir veb tətbiqi</footer>
        </div>
    </body>
    </html>
    
    
    ''' 
@app.route('/surname')
def only_surname():
    soyad=namess.get_surname()
    return f'''
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yalnız Soyad</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #e0f7fa;
                color: #333;
            }}
            .container {{
                width: 90%;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                text-align: center;
            }}
            h1 {{
                color: #00796b;
                margin-bottom: 20px;
            }}
            .content {{
                margin-top: 20px;
                font-size: 18px;
                color: #004d40;
            }}
            .button {{
                display: inline-block;
                padding: 15px 25px;
                font-size: 18px;
                color: #fff;
                background-color: #00796b;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin-top: 20px;
                transition: background-color 0.3s;
            }}
            .button:hover {{
                background-color: #004d40;
            }}
            footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #00796b;
            }}
        </style>
    </head>
    <body>
        
        <div class="container">
            <h1> <i class="bi bi-arrow-clockwise"></i> Yalnız Soyad:</h1>
            <div class="content">
                <strong>{soyad}</strong>
            </div>
            <a class="button" href="/">Ana Səhifəyə Dön</a>
            <footer>Flask ilə hazırlanan bir veb tətbiqi</footer>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </div>
    </body>
    </html>



    '''
@app.route('/zer')
def  rolldice():
    dice2=dice.roll_dice()
    dice1=dice.roll_dice()
    return f'''         <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Roll Dice</title>
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
                text-align: center;
                color: #fff;
                padding: 50px;
            }}
            h1 {{
                font-size: 3em;
                margin-bottom: 20px;
            }}
            .dice-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 20px;
                margin-top: 20px;
            }}
            .dice {{
                width: 100px;
                height: 100px;
                display: flex;
                justify-content: center;
                align-items: center;
                border: 2px solid #fff;
                border-radius: 10px;
                font-size: 2em;
                background-color: #ffffff33;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            }}
            button {{
                margin-top: 20px;
                padding: 15px 30px;
                font-size: 1.2em;
                cursor: pointer;
                border: none;
                background-color: #ff7e5f;
                color: white;
                border-radius: 25px;
                transition: background-color 0.3s;
            }}
            button:hover {{
                background-color: #feb47b;
            }}
        </style>
    </head>
    <body>
        <h1>Roll the Dice</h1>
        <div class="dice-container">
            <div class="dice">{dice1}</div>
            <div class="dice">{dice2}</div>
        </div>
        <button onclick="location.reload()">Roll Again</button>
    </body>
    </html>
    '''

app.run(port=5151, debug=True, host='localhost')
