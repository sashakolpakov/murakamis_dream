from pathlib import Path
p=Path('/private/tmp/murakamis_dream-publication/book/chapters/methods.md')
s=p.read_text()
def replace(old,new):
 global s
 assert s.count(old)==1, (s.count(old),old[:110])
 s=s.replace(old,new)
def after(old,new):
 replace(old,old+'\n\n'+new)
after('The [notation chapter](notation.md) gives the conventions used in the detailed calculations.',
"The starting references are Kashaev's [definition of the invariant](https://arxiv.org/abs/q-alg/9504020) and [volume proposal](https://arxiv.org/abs/q-alg/9601025). The [Murakami–Murakami paper](https://arxiv.org/abs/math/9905075) relates it to the colored Jones formulation. The finite invariant used here is specified directly; that relation is not a replacement for the source calculations.")
replace('For an unchanged general matched sphere,','For an unchanged matched simple sphere with the stated Morse presentation and markings,')
after('The [geometry chapter](geometry.md) explains the actual cells, cusp markings, and smooth fillings used in this project.',
"For the precise standard criterion on an orientable manifold with torus boundary, see [Futer and Guéritaud, *From angled triangulations to hyperbolic structures*, Definition 3.1 and Theorem 1.2](https://arxiv.org/pdf/1004.0440). [Rivin's 1994 paper](https://annals.math.princeton.edu/1994/139-3/p02) gives the earlier variational setting. The marked gluing proof linked above establishes the version used by this source rather than inferring it from the appearance of a dilogarithm.")
after('It does not say that one Fourier coefficient equals the norm or that the phases of several contributions agree.',
'For background on finite-group transforms and their normalization, see [Terras, *Fourier Analysis on Finite Groups and Applications*](https://doi.org/10.1017/CBO9780511626265).')
replace(r'In the actual color transform, the vector \(c\) is fixed by the original colored evaluation and its normalization.',
r'In the actual color transform, put \(c_0=K_N(K)\) and \(c_j=C_j(q_N)\) for \(1\le j<N\), where \(C_j\) is the original reduced, zero-framed ordinary-color evaluation.')
after(r'If \(\log E_N/N\to\lambda>0\), then the Kashaev volume rate is \(\pi\lambda\).',
r'In particular \(C_1=1\), explaining the lower bound on \(R_N^{\mathrm{ord}}\). The ordinary-color bound uses the actual reduced root evaluation and its finite unitary realization, including the normalization cost.')
replace('The [regulator-majorization note](../../notes/regulator_majorization_and_source_energy.md) proves the relevant inequalities and gives a stronger sufficient condition: an actual positive transport must preserve the regulator observable, not merely its total mean. That extra property has not been established for the general knot connection.',
'The [regulator-majorization note](../../notes/regulator_majorization_and_source_energy.md) proves the relevant inequalities and gives a stronger sufficient criterion. One crucial input is a bistochastic positive transport that fixes the regulator observable: it preserves both identity and trace, as well as that specified observable. The criterion also retains its action factorization and endpoint costs. These properties have not been established for the general knot connection.')
after('These properties have not been established for the general knot connection.',
"The standard majorization definitions are developed in [Marshall, Olkin, and Arnold, *Inequalities: Theory of Majorization and Its Applications*](https://link.springer.com/book/10.1007/978-0-387-68276-1). The matrix product result goes back to [Horn, *On the singular values of a product of completely continuous operators*](https://doi.org/10.1073/pnas.36.7.374). [Tao, Jeong, and Gowda](https://userpages.umbc.edu/~gowda/papers/trGOW20-02.pdf) discuss that matrix statement before developing its Jordan-algebra analogues.")
after('The completed pretzel argument obtains its estimates directly and does not assume these missing Tauberian hypotheses.',
"For the positive-measure statement, see [Michael Taylor, *Karamata's Tauberian Theorem*, §1](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/07/karamata.pdf). The linked local criterion gives a direct moment proof of the power-law case and explains the additional hypothesis needed at individual quantum levels.")
after('Thus neither diagonalizing each matrix separately nor naming a dominant classical branch is a substitute for controlling their ordered product.',
"Local stationary-phase methods are treated in [Hörmander, *The Analysis of Linear Partial Differential Operators I*](https://link.springer.com/book/10.1007/978-3-642-61497-2). A related root-of-unity asymptotic problem is [Garoufalidis and Zagier's Nahm-sum analysis](https://arxiv.org/abs/1812.07690). Its fixed-root radial limit and hypotheses differ from the growing-order roots and finite knot sums here; no identification of those objects is assumed.")
after('specifies a possible longitude as the meridian varies. It does not select the quantum invariant.',
'The classical reference is [Cooper, Culler, Gillet, Long, and Shalen, *Plane curves associated to character varieties of 3-manifolds*](https://homepages.math.uic.edu/~culler/papers/PlaneCurves/curves.pdf). The peripheral basis and the choice between eigenvalues and squared eigenvalues are part of the definition.')
after(r'Expressing an already proved limit through that recurrence is different from proving that an arbitrary quantization of the classical \(A\)-polynomial has the same limit.',
"Prior recurrence results include [Garoufalidis and Lê on colored-Jones q-holonomicity](https://arxiv.org/abs/math/0309214) and [Brown, Dimofte, Garoufalidis, and Geer on the ADO family](https://arxiv.org/abs/2005.08176). The latter's Theorem 4.4 retains an explicit framing and variable substitution. [Wilf and Zeilberger's multisum theory](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/multiwz.html) provides the general creative-telescoping background. The local finite-source proof retains the actual boundary and root-normal data. These references do not supply a general identification of the classical geometric component. The proposed characteristic/deformation comparison is formulated in [Garoufalidis's 2004 paper](https://arxiv.org/abs/math/0306230).")
after('It does not automatically choose the original quantum period or justify descent of its normalization.',
'For torsors in algebraic families, one must also specify the base and the topology in which local sections exist; see [Stacks Project, §39.11](https://stacks.math.columbia.edu/tag/0497). The elementary examples above have explicit fibers and actions.')
replace(r'For an ideal tetrahedron with shape \(z\in\mathbb C\setminus\{0,1\}\), the real volume is its Bloch–Wigner dilogarithm',
r'For an oriented ideal tetrahedron with shape \(z\in\mathbb C\setminus\{0,1\}\), the signed volume is its Bloch–Wigner dilogarithm')
after('A **regulator** here is the map taking the algebraic tetrahedral data, with their relations and markings, to the corresponding volume or complex period.',
r"The volume is positive for the positive orientation \(\operatorname{Im}z>0\). [Neumann's extended Bloch-group paper](https://arxiv.org/abs/math/0307092) explains how logarithmic lifts enter the complex regulator. The ordinary Bloch–Wigner volume and that lifted complex quantity must be distinguished.")
after('The [regulator and completion proof](../../notes/general_source_regulator_hyperbolic_equality.md) gives this argument in detail.',
"The standard peripheral deformation and volume-potential framework is [Neumann and Zagier, *Volumes of hyperbolic three-manifolds*](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1016/0040-9383(85)90004-7/fulltext.pdf). The signs, primitive periods, and eigenvalue-versus-ratio convention in the displayed filling equation come from the local marked proof, not from an unrecorded change of that reference's coordinates.")
after('These local tetrahedra are comparison cells. Their existence alone does not identify a glued knot complement.',
r"The local \(6j\)-volume relation is established literature: see [Costantino, *6j-symbols, hyperbolic structures and the Volume Conjecture*](https://arxiv.org/abs/math/0611399) and [Costantino and Murakami's non-integral representation model](https://arxiv.org/abs/1005.4277). The [coverage comparison](../../notes/literature_hyperideal_racah_volume_coverage.md) records the root substitutions, supported angle ranges, and different regularizations. No novelty is claimed for the general local-volume mechanism.")
replace('<!-- Primary-source references are inserted after the coverage check. -->',r"""The citations beside the methods identify the relevant statement and its role. For a first reading, the following sequence is useful:

1. **Invariant and volume question:** Kashaev's 1995 definition and 1997 volume paper, followed by Murakami–Murakami for the colored Jones relation.
2. **Geometric optimization:** Rivin's variational paper and Futer–Guéritaud for angle structures, allowed tangent directions, and the precise critical-point criterion.
3. **Norm estimates:** Terras for finite Fourier analysis; Marshall–Olkin–Arnold and Horn for majorization and product singular values. Weighted Cauchy and finite Parseval are proved explicitly above.
4. **Cross-level asymptotics:** Taylor's Tauberian notes. Compare the cumulative conclusion with the additional source-transport condition in the local criterion.
5. **Recurrences:** Wilf–Zeilberger for multisum elimination, then the colored-Jones and ADO papers for the objects and conventions concerned. Keep the classical A-curve and the proposed characteristic comparison separate.
6. **Regulators and peripheral geometry:** Neumann–Zagier for the local deformation potential, Neumann for logarithmic regulator data, and the explicit torsor definitions for any claimed group action.
7. **Local asymptotics versus a whole knot period:** Costantino's \(6j\)-volume result and the Nahm-sum comparison illustrate related problems with different normalizations and limiting regimes. The complete-source estimates and contour arguments remain the additional work in this project.

The literature search is a coverage and attribution check. It does not turn an external paper into an unchecked proof input, or turn a local calculation into a theorem about an arbitrary knot. The manuscript states the actual hypotheses and supplies the arguments used for its conclusions.""")
p.write_text(s)
p=Path('/private/tmp/murakamis_dream-publication/notes/regulator_majorization_and_source_energy.md')
s=p.read_text()
s=s.replace('[Gowda, Some log and weak majorization inequalities]','[Tao, Jeong, and Gowda, Some log and weak majorization inequalities in Euclidean Jordan algebras]')
p.write_text(s)
print('Methods references and scope corrections written.')

