from app import create_app


app = create_app()

if __name__ == '__main__':
    # threaded=True 表示开启单进程多线程模式
    app.run(host='0.0.0.0',debug=app.config['DEBUG'], threaded=True)
    