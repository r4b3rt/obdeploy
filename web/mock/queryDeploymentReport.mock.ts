// @ts-ignore
import { Request, Response } from 'express';

export default {
  'GET /api/v1/deployments/:name/report': (req: Request, res: Response) => {
    res.status(200).send({
      code: 75,
      data: {
        total: 64,
        items: [
          {
            name: '钱霞',
            type: 176,
            version: '有证派正都为理南多流手党道学的器。',
            servers: [
              '得例界管区平节及根件青委号定。',
              '生中国极心界通提道备算连。',
              '论参传关消验反主好派层备区志局即。',
              '风据热界就南情委置能口龙。',
              '应来料开离及入好南维族并军效容京光。',
              '物入素实用容手在圆公料地放斗。',
              '儿条这管性增量步此接数红制难道上气。',
              '效组温由斯点根反自做可响。',
              '况造利专边由应再导民海马油此决叫转队。',
              '感值将素织广气满真感族为王。',
              '往选族感王计将温公题本热联经况。',
              '连手内山去第安名新看论外总民对基。',
            ],
            status: 'error',
          },
          {
            name: '姜超',
            type: 177,
            version: '称用后展身走单金改委素在往国适越。',
            servers: [
              '见四建称段则些几候种千种几。',
              '素间解院第织图任但被活行导或量适。',
              '马好出空少民平两示后两导志料果内。',
              '置正证难际即个使至身者机统厂些。',
              '等上决技它万张打当积住满很只素。',
              '在便七积下思感广石由思布影。',
              '管管际生共思支物带团取称社界代常据只。',
              '深区较史理识米指包问写国统建很。',
              '料决而与近常般表照系油应周。',
              '般强住海片节应北感低中什第边美。',
              '海然风个题场手又特型保样必会体转才性。',
              '度备点即素装节外前门党什音过须。',
            ],
            status: 'default',
          },
          {
            name: '潘磊',
            type: 178,
            version: '京响行保没口在七织与动就较复院运。',
            servers: [
              '叫要究正法统回起能家新使着月江。',
              '相标红白进常别须铁级由二求一反。',
              '把结组体压思划际度常连起由取近。',
              '就所江矿存革法劳治满白类。',
              '她位生增是光和活共向制局取常用。',
              '且感真因七路与军各及划做求计快展。',
              '习里天直强先公义算因所拉什。',
              '世品用十条接几规题准目为都。',
              '万表求极和集达量加角铁况。',
              '法斯间用局日厂实音造厂学带商工关。',
              '然响称存指指安解老着度通周西西加。',
              '观起声形对型置把政数对理命院名名基。',
            ],
            status: 'default',
          },
        ],
      },
      msg: '运石听集大周去里新说军太合。',
      success: true,
    });
  },
};
