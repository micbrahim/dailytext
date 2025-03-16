import scraper
import sys

def main():
    if len(sys.argv) != 2:
        print("invalid length")
        exit(1)
    number = int(sys.argv[1])
    if not (isinstance(number, int)):
        print("invalid number")
        exit(1)
    scraper.send_imessage(number, scraper.wikipedia())
    print("message sent")

if __name__ == "__main__":
    main()