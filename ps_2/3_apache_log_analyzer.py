# 3. Log File Analyzer:
#  Create a script that analyzes web server logs (e.g., Apache, Nginx) for
#  common patterns such as the number of 404 errors, the most requested
#  pages, or IP addresses with the most requests. The script should output a
#  summarized report.



import re
class ServerReportGenerator:
    def __init__(self,log_path):
        self.log_path=log_path
        if not os.path.exists(self.log_path):
            raise FileNotFoundError(f"The file {self.log_path} does not exist.")
        self.log_pattern = re.compile(
    r'(?P<ip>[\d.]+) - - \[(?P<date>[\w:/]+)\s[+\-]\d{4}\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\d+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
)
            
    def _parse_log_line(self,line):
        """
        This function matches the pattern for the line from log file
        """
        match = log_pattern.match(line)
        if match:
            return match.groupdict()
        return None
    def analyze_log_file(self,log_entries):
        """
        this function analyzes the log file to create the report of required things
        """
        # Counters for different analysis
        status_counter = Counter()
        page_counter = Counter()
        ip_counter = Counter()

        for entry in log_entries:
            status_counter[entry['status']] += 1
            request = entry['request'].split(' ')
            if len(request) > 1:
                page_counter[request[1]] += 1
            ip_counter[entry['ip']] += 1

        # Generate the report
        report = {
            'total_requests': len(log_entries),
            'status_counts': status_counter,
            'most_requested_pages': page_counter.most_common(10),
            'ip_addresses_with_most_requests': ip_counter.most_common(10),
        }

        return report
    
    def create_report(self):
        """
        top level function to create report
        """
        with open(self.log_path, 'r') as file:
            log_entries = [self._parse_log_line(line) for line in file if self._parse_log_line(line)]
        report = self.analyze_log_file(log_entries)
        report_str = f"Total Requests: {report['total_requests']}\n"

        report_str += "\nStatus Codes:\n"
        for status, count in report['status_counts'].items():
            report_str += f"  {status}: {count}\n"

        report_str += "\nMost Requested Pages:\n"
        for page, count in report['most_requested_pages']:
            report_str += f"  {page}: {count}\n"

        report_str += "\nIP Addresses with Most Requests:\n"
        for ip, count in report['ip_addresses_with_most_requests']:
            report_str += f"  {ip}: {count}\n"

        return report_str

        
if __name__ == "__main__":
    path = "apache_logs.log"
    g = ServerReportGenerator(path)
    report = g.create_report()
    print(report)