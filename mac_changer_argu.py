import subprocess
import optparse

parser = optparse.OptionParser()
#static command line of optparser
parser.add_option("-i", "--interface",dest="interface",help="interface to change its MAC address")
parser.add_option("-m", "--mac",dest="new_mac",help="new MAC address")
(option, argument) = parser.parse_args()
#command line to pass the argument

interface = option.interface
new_mac = option.new_mac

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
print("mac changed successfully!!")