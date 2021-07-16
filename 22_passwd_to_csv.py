import csv

def passwd_to_csv(passwd_file, csv_out):
    with open(csv_out, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter="\t")
        with open(passwd_file) as passwd_f:
            for line in passwd_f:
                if line.startswith("#"):
                    continue
                split = line.split(":")
                csv_writer.writerow([split[0], split[2]])

passwd_to_csv('/etc/passwd', 'testing_passwd_csv')
