// @ts-ignore
import { Request, Response } from 'express';

export default {
  'GET /api/v1/deployments/:name/precheck': (req: Request, res: Response) => {
    res.status(200).send({
      code: 75,
      data: {
        total: 61,
        finished: 98,
        all_passed: false,
        status: 'default',
        message: '温千着除电处每价花这题为持按回采。',
        info: [
          {
            name: '金丽',
            server: '转压队规他难层却只从着无铁往。',
            status: 'success',
            result: '改没到称深很了流先低五各好反才。',
            recoverable: false,
            code: '然响空图被收定教她在争工易道。',
            description: '年争深除意题样人油很技几变只规天布。',
            advisement: null,
          },
          {
            name: '叶平',
            server: '还者代日例场由族则广今建。',
            status: 'processing',
            result: '儿红己多我步技工即正子万据。',
            recoverable: false,
            code: '单断然共设打根应地眼面四金族更根。',
            description: '红二员步条生少做山极全备。',
            advisement: null,
          },
          {
            name: '秦杰',
            server: '路查达地南最外属着小儿参区。',
            status: 'processing',
            result: '长按委物调身任律后写领断海白。',
            recoverable: true,
            code: '象细济月种色区权状话花又整增制条。',
            description: '进般记形对育内有则信府最生心角。',
            advisement: null,
          },
          {
            name: '袁霞',
            server: '变律证必角水群片按系新料等育。',
            status: 'success',
            result: '提本认路变导议意二们共参规声收叫代。',
            recoverable: true,
            code: '素写干难者没位带达名火形部七。',
            description: '由响立料现见质达产治品济打带生。',
            advisement: null,
          },
          {
            name: '陆伟',
            server: '群别党需元质相多么声要系报准。',
            status: 'error',
            result: '条在风置立效其较京实国半名一。',
            recoverable: false,
            code: '步状规好交们带应难江内花能组。',
            description: '结理合几般学比受率是走年头。',
            advisement: null,
          },
          {
            name: '田杰',
            server: '组济当回史适量主因内广去报值然。',
            status: 'error',
            result: '王明老圆相长展工长条器图快主达都问。',
            recoverable: true,
            code: '走条面在住极般龙复参料程积今科圆同。',
            description: '山石细色写酸气也却些米即四局构前管。',
            advisement: null,
          },
          {
            name: '朱秀英',
            server: '太那置拉土现光风五会立天果影设。',
            status: 'default',
            result: '才而很治海现业家照交写精商。',
            recoverable: false,
            code: '分生矿划规门准列业则路从格群经根须。',
            description: '劳部新保入光正方空马九界千。',
            advisement: null,
          },
        ],
      },
      msg: '车值二清平打经值见型查龙划边示江质。',
      success: true,
    });
  },
};