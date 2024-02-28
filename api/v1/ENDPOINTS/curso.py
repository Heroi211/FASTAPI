from typing import List

from fastapi import status, APIRouter,Depends,HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schemas import CursoSchema

from core.deps import get_session()

router = APIRouter()

router.post('/',status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def postCurso(curso:CursoSchema,db: AsyncSession = Depends(get_session())):
    novo_curso = CursoModel(titulo = curso.titulo,
                            aulas = curso.aulas,
                            horas = curso.horas)
    db.add(novo_curso)
    await db.commit
    return novo_curso


router.get('/', status_code=status.HTTP_200_OK,response_model=List[CursoSchema])
async def getCursos(db:AsyncSession = Depends(get_session())):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos:List[CursoModel] = result.scalars().all()
        
        return cursos