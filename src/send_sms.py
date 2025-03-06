from src.cli import cli


def main():
    send_num, rec_num, text_sms = cli()
    print(send_num, rec_num, text_sms)




if __name__ == '__main__':
    main()