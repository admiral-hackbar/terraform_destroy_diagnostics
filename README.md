# terraform_destroy_diagnostics
Small python tool to diagnose the output from terraform destroy or apply, when it doesn't work.

I ran into problems with terraform destroying things out of order on AWS. Some things wouldn't get destroyed, and threw unhelpful messages. It was hard to parse the terraform output to see what had begun destroying, but didn't complete, so this script parses that output and finds those objects.

In order to use the script, record your output from terraform to a file (you can possibly pipe to it instead if you specify the file as stdin), then pass that file as the argument to the script (python destroyed_terraform.py <filename>). When recording the output, you probably also want to send the stderr output as well. (when running terraform destroy, append `2>&1 | tee <filename>`).
