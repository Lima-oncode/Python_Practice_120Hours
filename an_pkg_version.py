import sys
import pkg_resources

print(pkg_resources.get_distribution("pandas").version)