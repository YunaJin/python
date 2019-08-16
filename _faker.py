from faker import Faker
from faker.providers import internet

#faker=Faker()
faker=Faker('zh-CN')
faker.seed(10)
print('name:',faker.name())
print('address:',faker.address())
print('text:',faker.text())
print('ssn:',faker.ssn(min_age=16,max_age=28))
print(faker.profile(fields=None, sex=None))
print('*'*20)
print(faker.simple_profile(sex=None))


#internet
print('image url:',faker.image_url())
print('explorer:',faker.internet_explorer())
print('IPv4:',faker.ipv4())
print('IPv6:',faker.ipv6())
print('IPv4 private:',faker.ipv4_private())
print('IPv4 public:',faker.ipv4_public())