from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')

    if log == "critical":
        app.logger.critical("It's Critical!!!")
    elif log == 'warning':
        app.logger.warning("I'm warning you!")
    elif log == 'error':
        app.logger.error("Error! Error! Error!")
    else:
        app.logger.info("Friendly info")

    return render_template(
        'index.html',
        log=log
    )
