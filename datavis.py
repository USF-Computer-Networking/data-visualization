import os, time, subprocess
import turtle



def get_ip():

    def run_command_silently(command):
        with open(os.devnull, 'wb') as devnull:
            subprocess.check_call(command.split(' '), stdout=devnull, stderr=subprocess.STDOUT)

    run_command_silently('ping -c 1 255.255.255.255')
    time.sleep(0.5)
    arp_entries = subprocess.check_output(('arp','-na')).splitlines()
    all_ip = []

    for entry in arp_entries:
        ip_addr, rest = entry.split('(')[1].split(') at ')
        all_ip.append((ip_addr))

    for ip in all_ip:
        print 'IP:', ip

    data_visualization(all_ip)


def data_visualization(addrs):
    tboy = turtle.Turtle()
    angle = 360 / len(addrs)
    turtle.bgcolor("#5BFF33")
    tboy.pu()
    tboy.setpos(-100, -100)
    tboy.pd()
    for x in range(len(addrs)):
        tboy.fd(200)
        tboy.write(addrs[x], align="center", font=("Arial", 12, "bold"))
        tboy.lt(angle)

    turtle.done()

def main():

    print("Starting scan...")

    get_ip()

if __name__ == '__main__':
    main()