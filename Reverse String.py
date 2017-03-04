s='Rob Hall, a mountaineering guide from New Zealand who had ascended Everest four times previously, understood as well as anybody the need to get up and down quickly. Recognizing that the basic climbing skills of some of his clients were highly suspect, Hall intended to rely on fixed lines to safeguard and expedite our group over the most difficult ground. The fact that no expedition this year had been to the top yet concerned him, therefore, because it meant that ropes had not been installed over much of this terrain. On the morning of our summit bid, the only ropes that had been strung along the precipitous serrations of the upper Southeast Ridge were a few ancient, tattered remnants from past expeditions that emerged sporadically from the ice. Anticipating this possibility before leaving Base Camp, Hall and Scott Fischer, the leader of another commercial expedition, convened a meeting attended by guides from both teams, during which they agreed that each expedition would dispatch two Sherpas — including their climbing sirdars, Ang Dorje and Lopsang Jangbu — from Camp Four ninety minutes ahead of the main groups. This would give the Sherpas time to install fixed lines on the most exposed sections of the upper mountain before the clients arrived. “Rob made it very clear how important it was to do this,” recalls Neal Beidleman, a guide from Fischer’s expedition who participated in the meeting. “He wanted to avoid a time-consuming bottleneck at all costs.” For some unknown reason, however, no Sherpas had departed ahead of us when we left camp and started climbing toward the summit. Perhaps the violent gale that had struck the mountain on May 9, and hadn’t stopped blowing until 7:30 P.M., prevented the Sherpas from mobilizing as early as they’d hoped. After the expedition, Lopsang insisted that at the last minute Hall and Fischer had simply scrapped the plan to fix ropes in advance of their clients, because they’d received erroneous information that the Montenegrins had already completed the job as high as the South Summit. But if Lopsang’s assertion is correct, neither Beidleman, nor Anatoli Boukreev (Fischer’s senior guide), nor Mike Groom (Hall’s senior guide), were ever told of the altered scheme. And if the plan to fix lines had been intentionally abandoned, there would have been no reason for Lopsang and Ang Dorje to depart with the 300 feet of rope that each Sherpa carried when they set out from Camp Four at the front of their respective teams. In any case, no ropes had been fixed ahead of time on the upper reaches of the mountain. At 5:30 A.M., when Ang Dorje and I first arrived on a promontory known as the Balcony at 27,600 feet, we were more than an hour in front of the rest of Hall’s group. At that point we could easily have gone ahead to install the ropes. But Rob had explicitly forbidden me to go ahead, and Lopsang was still far below, short-roping a client named Sandy Pittman, so there was nobody to accompany Ang Dorje. Quiet and moody by nature, Ang Dorje’s disposition seemed especially somber as we sat together watching the sun come up in the sub-zero cold. My attempts to engage him in conversation went nowhere. His ill humor, I figured, was perhaps due to the abscessed tooth that had been causing him pain for the previous two weeks. Or maybe he was brooding over the disturbing vision he’d had four days earlier: On their last evening at Base Camp, Ang Dorje and some other Sherpas had celebrated the coming summit attempt by drinking a large quantity of chhang — a thick, sweet beer brewed from rice and millet. The next morning, severely hungover, he was extremely agitated; before ascending the Ice Fall he confided to a friend that he’d seen ghosts in the night. An intensely spiritual young man, Ang Dorje was not one to take such portents lightly.'
'''
方法一
'''
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.b=''
        for i in range(len(s)-1,-1,-1):
            self.b+=s[i]
        return self.b
'''
'''
方法二
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        self.l=list(s)
        self.l.reverse()
        self.l=''.join(self.l)
        return self.l


m=Solution()
d=m.reverseString(s)
print(d)
#方法二能被OJ接受
#但方法一不知道为什么不能通过OJ，我觉得测试用例有点问题，也可能我没彻底理解题意
