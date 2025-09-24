from django.shortcuts import render, HttpResponse

def hello(requast):
    return HttpResponse("""
                        <!DOCTYPE>
                        <head>
                        </head>
                        <body>
                        <div style="background-color: red;">
                        <ul>
                            <li>
                            Hola
                        </li>
                        </ul>
                        </div>
                        </body>
                        
                        """)