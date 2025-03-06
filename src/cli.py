import argparse


def cli()-> (int, int, str):
    parser = argparse.ArgumentParser(description="Send sms")
    parser.add_argument('send_num', type=int, help="Sender number")
    parser.add_argument('rec_num', type=int, help="Recipient number")
    parser.add_argument('text_sms', type=str, help="Text SMS")
    args = parser.parse_args()

    return args.send_num, args.rec_num, args.text_sms