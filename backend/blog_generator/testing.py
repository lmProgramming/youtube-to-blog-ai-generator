import re
import os

t = '''
#Title: The Case for Legalizing Cannabis: A Closer Look at Vice President Harris's Stance

#Content:
In a recent discussion, Vice President Kamala Harris expressed a strong belief that individuals should not be incarcerated for using marijuana. This viewpoint is part of a broader conversation surrounding the legalization of cannabis and the implications of criminalizing its use. Harris stated, "I just feel strongly people should not be going to jail for smoking weed."

Her position aligns with the growing sentiment that criminalizing marijuana use has had significant social and racial repercussions, disproportionately affecting certain communities. Historically, individuals from marginalized backgrounds have been the primary targets of anti-drug policies, leading to mass incarceration and perpetuating systemic inequalities.

Furthermore, Harris emphasized the need to shift towards a more progressive approach by legalizing cannabis instead of perpetuating a cycle of criminalization. She highlighted, "I just think we have come to a point where we have to understand that we need to legalize it and stop criminalizing this behavior."

This stance is not new for Vice President Harris, who has long advocated for the legalization of marijuana. Her consistent support for this cause reflects an understanding of the complex interplay between drug policy, social justice, and public health.

The debate over the legalization of cannabis is multifaceted, touching on issues of personal freedom, criminal justice reform, and economic opportunities. Proponents argue that legalizing marijuana can lead to a reduction in arrests, generate tax revenue, and create new jobs in the burgeoning cannabis industry. On the other hand, opponents express concerns about potential health risks, impaired driving, and the impact on youth.

As attitudes towards cannabis continue to evolve across the country, Vice President Harris's position adds a prominent voice to the discussion. By advocating for the legalization of marijuana and emphasizing the need to move away from punitive measures, she is contributing to a broader dialogue on drug policy reform and social equity.

In conclusion, Vice President Kamala Harris's call to legalize marijuana reflects a commitment to addressing the harmful consequences of criminalization and advancing a more equitable approach to drug policy. As the conversation around cannabis legalization unfolds, her stance serves as a catalyst for further debate and action in this evolving landscape.
'''

generated_blog = t.strip()

title_match = re.search(r"#Title:\s*(.*)", generated_blog)
content_match = re.search(r"#Content:\s*(.*)", generated_blog, re.DOTALL)

if not title_match or not content_match:
    raise Exception('Blog generation failed - could not find title or content')

title = title_match.group(1)
content = content_match.group(1)

print(title)
print(content)