# The positive prism boundary and its growing radial path

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The dilogarithmic action of the initialized centered tensor has an
exact boundary interpretation in the already constructed ideal prism.
Its imaginary part is the negative Newton prism action; its real part
is a specified linear phase. Moreover the entire radial segment from
the origin to every strict positive prism boundary point lies on the
growing side of this action.

There is also an exact finite-source interpretation of the physical
boundary grid. A centered generating packet on that grid selects one
Newton basis vector. Three such packets therefore recover the positive
Newton tensor, including its full repeated-root algebra and original
Frobenius closing. These statements connect the geometric boundary
symbol to the initialized source near the origin. They do not prove
transport of its asymptotic through the whole disk or uniformly onto
the unit boundary.

## 1. The strict prism domain and its original face labels

Let
\[
 \mathcal P=\{\mathbf x\in\mathbb R^3:
     x_i>0,\quad x_i+x_j<1\ (i\ne j),\quad
     S:=x_1+x_2+x_3>1\}.
 \tag{1}
\]
Then \(x_i<1\) and \(1<S<3/2\). Define
\[
 L(u)=\int_0^u\log(2\sin\pi v)\,dv\quad(0<u<1),
 \qquad
 \tau(\mathbf x)=\sum_{i<j}L(x_i+x_j)
                     -\sum_iL(x_i)-L(S-1).
 \tag{2}
\]
All arguments in this formula lie strictly between zero and one.

The original directed Newton multiplication has action
\[
 m(a,b,c)=L(a+b)+L(c)-L(a)-L(b)
              -L(c-a)-L(c-b)-L(a+b-c).
 \tag{3}
\]
Set its two input labels to \(a=x_1,b=x_2\) and its output
label to \(c=1-x_3\). Conditions (1) are exactly its strict
support conditions. The reflection identity \(L(1-u)=-L(u)\)
gives
\[
                    \tau(\mathbf x)=m(x_1,x_2,1-x_3).
 \tag{4}
\]
The ideal-prism theorem constructs a convex ideal triangular prism
with these directed, ordered quadrilateral faces and proves
\[
                  \operatorname{Vol}(\operatorname{Prism}_{\mathbf x})
                                      =\pi\tau(\mathbf x).
 \tag{5}
\]
The complement \(1-x_3\) is required by the original Frobenius
pairing of an output with the third leg. It is not an unrecorded
permutation or mutation of the ordered prism faces.

## 2. The complete action on the unit boundary

Use the initialized centered action
\[
 \Psi(\mathbf t)=-\frac{\pi}{12}
 +\frac1{2\pi}\left[
       \sum_i\operatorname{Li}_2(-t_i)
       +\operatorname{Li}_2(-t_1t_2t_3)
       -\sum_{i<j}\operatorname{Li}_2(t_it_j)\right].
 \tag{6}
\]
Its branches start from the power series on the unit polydisk.
For \(\mathbf x\in\mathcal P\), put
\[
                  t_i(r)=-r e^{-2\pi i x_i},\qquad 0\le r\le1.
 \tag{7}
\]
None of the dilogarithm arguments at \(r=1\) is one: this follows
from \(0<x_i,x_i+x_j<1\) and \(1<S<3/2\). Thus (6) has
the indicated continuous, locally analytic boundary value.

**Theorem 1.** With the branches in (6)--(7),
\[
 \boxed{\quad
 i\Psi(\mathbf t(1))
       =\tau(\mathbf x)+i\pi(1-S).
 \quad}
 \tag{8}
\]
In particular
\[
 -\operatorname{Im}\Psi(\mathbf t(1))=\tau(\mathbf x),
 \qquad
 -2\pi\operatorname{Im}\Psi(\mathbf t(1))
                     =2\operatorname{Vol}(\operatorname{Prism}_{\mathbf x}).
 \tag{9}
\]
The factor two in the latter equation has not been absorbed into
the prism volume.

**Proof.** The elementary unit-circle dilogarithm formula is
\[
 \operatorname{Im}\operatorname{Li}_2(e^{2\pi iu})
                              =-2\pi L(u)\quad(0<u<1).
 \tag{10}
\]
It follows by differentiating the absolutely convergent Abel
series, using
\(\operatorname{Re}\log(1-e^{2\pi iu})=\log(2\sin\pi u)\),
and fixing the value at zero. At (7), the three types of
arguments in (6) are
\[
 e^{-2\pi i x_i},\qquad e^{-2\pi i S},\qquad
 e^{-2\pi i(x_i+x_j)} .
\]
Reflection in (10), and periodicity for \(S\), prove
\(\operatorname{Im}\Psi=-\tau\).

The real part follows from
\[
 \operatorname{Re}\operatorname{Li}_2(e^{2\pi iu})
       =\pi^2B_2(u),\qquad
 B_2(u)=u^2-u+\tfrac16,\qquad 0\le u\le1.
 \tag{11}
\]
One may derive (11) by integrating the Fourier series
\(\sum_{n\ge1}\sin(2\pi nu)/n=\pi(1/2-u)\);
its constant is \(\sum n^{-2}=\pi^2/6\).
The required Bernoulli combination is
\[
 \sum_iB_2(x_i)+B_2(S-1)-\sum_{i<j}B_2(x_i+x_j)
                                              =-2S+\tfrac{13}{6}.
\]
Including the constant \(-\pi/12\) in (6) therefore gives
\(\operatorname{Re}\Psi=\pi(1-S)\), proving (8). \(\square\)

The logarithmic momenta retain a corresponding sign:
\[
 R_i(\mathbf t)=
 \frac{(1-t_it_j)(1-t_it_k)}
                  {(1+t_i)(1+t_1t_2t_3)},\qquad
 R_i(\mathbf t(1))=-e^{\partial_{x_i}\tau},
 \quad \{i,j,k\}=\{1,2,3\}.
 \tag{12}
\]
In fact the logarithm continued along (7) has the precise boundary
value
\[
 \partial_{x_i}\{i\Psi(\mathbf t(1))\}
                    =\partial_{x_i}\tau-i\pi .
 \tag{13}
\]
To check the sign directly, write every \(1-e^{-2\pi iu}\)
as \(2i e^{-\pi iu}\sin(\pi u)\). The three pair arguments
are in \((0,1)\), whereas \(S\in(1,3/2)\) has
\(\sin(\pi S)=-\sin(\pi(S-1))\). The phases cancel except
for this minus sign. The radial logarithms give the lift
\(-i\pi\), agreeing with (8).

These momenta also recover the actual ordered face metrics. In the
directed prism theorem,
\(\kappa_{\mathrm{in},1}=e^{-\partial_a m}\),
\(\kappa_{\mathrm{in},2}=e^{-\partial_b m}\), and
\(\kappa_{\mathrm{out}}=e^{-\partial_c m}\).
The complemented output in (4) therefore gives
\[
 \kappa_{\mathrm{in},1}=-R_1^{-1},\qquad
 \kappa_{\mathrm{in},2}=-R_2^{-1},\qquad
 \kappa_{\mathrm{out}}=-R_3 .
 \tag{13a}
\]
All three are positive on the prism boundary. Thus the signs and
the output complement identify these particular source momenta
with the old prism's ordered quadrilateral metrics, rather than
only with unmarked trace squares.

## 3. The entire strict prism has a growing radial path

**Theorem 2.** For every \(\mathbf x\in\mathcal P\),
\[
                  \operatorname{Im}\Psi(\mathbf t(r))<0
                                      \qquad(0<r\le1).
 \tag{14}
\]
The inequality is uniform away from zero on compact subsets of
\(\mathcal P\times(0,1]\).

**Proof.** Define the real radial Clausen function
\[
 F_a(u)=-\operatorname{Im}\operatorname{Li}_2(ae^{-2\pi iu}),
                                  \qquad 0<a\le1.
 \tag{15}
\]
It is periodic, \(F_a(1-u)=-F_a(u)\), and
\(F_a(0)=F_a(1/2)=0\). On \(0<u<1/2\) it is positive
and strictly concave. For \(a<1\), direct differentiation gives
\[
 F_a''(u)=
  -\frac{4\pi^2a\sin(2\pi u)}
                  {1-2a\cos(2\pi u)+a^2}<0.
 \tag{16}
\]
Concavity and the endpoint zeros imply positivity. The same
conclusions at \(a=1\) follow by continuity or direct
differentiation on this open angle interval. There is also
convexity in the logarithmic radius:
\[
 \frac{\partial^2}{\partial(\log a)^2}F_a(u)
          =\frac{a\sin(2\pi u)}
                  {1-2a\cos(2\pi u)+a^2}>0
                              \quad(0<u<1/2).
 \tag{17}
\]
Consequently
\[
                      F_r(u)+F_{r^3}(u)\ge2F_{r^2}(u).
 \tag{18}
\]

In these terms the quantity to prove positive is
\[
 -2\pi\operatorname{Im}\Psi(\mathbf t(r))
   =\sum_iF_r(x_i)+F_{r^3}(S-1)
                              -\sum_{i<j}F_{r^2}(x_i+x_j).
 \tag{19}
\]
If every \(x_i\le1/2\), each pair \(x_i+x_j=S-x_k>1/2\).
All pair terms on the right are therefore nonnegative after
their minus sign, all single terms are nonnegative, and
\(0<S-1<1/2\) supplies a strictly positive term. This proves
(14) in this part of the domain.

Otherwise exactly one angle is large. Relabel it
\(x_1=1-\delta>1/2\), and put
\[
 b=x_2,\quad c=x_3,\quad
 u=b+c-\delta,\quad p=\delta-b,\quad q=\delta-c,\quad s=b+c .
 \tag{20}
\]
Here
\[
 0<u<b,c<\delta<1/2,\qquad p,q>0,\qquad
 b+c=\delta+u,\qquad s=2u+p+q<1.
 \tag{21}
\]
By strict concavity, the pair \((b,c)\), with its fixed sum,
lies strictly between the more separated pair \((u,\delta)\).
Thus
\[
                 F_r(b)+F_r(c)-F_r(\delta)>F_r(u).
 \tag{22}
\]
Reflection rewrites (19) as
\[
 \begin{aligned}
 &F_r(b)+F_r(c)-F_r(\delta)+F_{r^3}(u)\\
 &\hspace{20mm}+F_{r^2}(p)+F_{r^2}(q)-F_{r^2}(s).
 \end{aligned}
 \tag{23}
\]
The first line is strictly larger than \(2F_{r^2}(u)\),
by (18) and (22). If \(s\ge1/2\), then \(F_{r^2}(s)\le0\)
and all other displayed terms needed for the bound are positive.
If \(s<1/2\), concavity with \(F_{r^2}(0)=0\) gives
subadditivity on this interval. Applying it repeatedly gives
\[
 2F_{r^2}(u)+F_{r^2}(p)+F_{r^2}(q)
                      \ge F_{r^2}(2u+p+q)=F_{r^2}(s).
 \tag{24}
\]
The strict inequality in (22) makes (23) positive in this case too.
This proves (14) on the whole domain. Uniformity on the stated
compact sets follows from continuity and strict positivity.
\(\square\)

## 4. The unit boundary is an exact positive source grid

The preceding action calculation has a finite counterpart.
At level \(N\ge2\), put \(d=N-1\), \(q=e^{\pi i/N}\),
\(\kappa=q^{d^2/2}\), and \(D_N(t)=1-(-1)^dt^N\).
All fractional powers mean these displayed exponentials.
Write \(s_j=\prod_{h=1}^j2\sin(\pi h/N)\), \(s_0=1\), and
\(T_N(\cos\theta)=\cos(N\theta)\).
The full algebra is \(H_N=\mathbb C[z]/(2T_N(z/2)+2)\), with
its original Frobenius row \(\phi\), normalized Newton basis
\(e_j=s_j^{-2}\prod_{h=0}^{j-1}(2\cos((2h+1)\pi/N)-z)\),
and centered basis \(f_a\). Its original generating tensor is
\[
 \mathcal C_N(\mathbf t)=
       \phi\!\left(\prod_{i=1}^3\sum_{a=0}^{d}f_a t_i^a\right).
 \tag{24a}
\]
For \(0\le j\le d\), put
\[
 x_{j,N}=\frac{j+1/2}{N},\qquad
 t_{j,N}=-e^{-2\pi i x_{j,N}},\qquad
 \gamma_{j,N}=\exp\!\left[-\frac{\pi i d}{N}(j-d/2)\right].
 \tag{25}
\]
Let \(e_j\) be the normalized full Newton basis and \(f_a\)
the centered basis. The exact centered Fourier matrix gives
\[
 \boxed{\qquad
       \sum_{a=0}^d f_a t_{j,N}^{\,a}
                                   =\sqrt N\,\gamma_{j,N}e_j .
 \qquad}
 \tag{26}
\]
Indeed the coefficient of \(e_\ell\) on the left is
\(N^{-1/2}e^{-\pi i d(\ell-d/2)/N}\)
times \(\sum_{a=0}^{N-1}e^{2\pi ia(\ell-j)/N}\).
The latter is \(N\delta_{\ell j}\).

For a triple \(\mathbf j=(j_1,j_2,j_3)\), let
\(T_{N,\mathbf j}=\phi(e_{j_1}e_{j_2}e_{j_3})\).
Consequently the original complete tensor obeys
\[
 \boxed{\quad
 \mathcal C_N(t_{j_1,N},t_{j_2,N},t_{j_3,N})
      =N^{3/2}\left(\prod_i\gamma_{j_i,N}\right)T_{N,\mathbf j}.
 \quad}
 \tag{27}
\]
There is no unknown closing coefficient in this identity.
The exact positive tensor is
\[
 T_{N,\mathbf j}
  =\frac{s_{j_1+j_2}s_{j_1+j_3}s_{j_2+j_3}}
       {N s_{j_1}s_{j_2}s_{j_3}s_{j_1+j_2+j_3-d}},
 \qquad s_a=\prod_{h=1}^a2\sin(\pi h/N),
 \tag{28}
\]
when each pair sum is at most \(d\) and the total is at least
\(d\), and is zero otherwise. These are the full-algebra
coefficients; no Casimir first normal was removed. Every grid
point \((x_{j_1,N},x_{j_2,N},x_{j_3,N})\in\mathcal P\)
satisfies the positive support conditions in (28).

The half-step offsets in (25) are important. The Newton indices
divided by \(N\) are \(x_i-1/(2N)\). The centered directed output
paired with \(j_3\) is exactly
\((d-j_3+1/2)/N=1-x_3\). Uniformly on compact subsets of
\(\mathcal P\),
\[
 \frac1N\log T_{N,\mathbf j}
                    =\tau(\mathbf x_{\mathbf j,N})
                                      +O(\log N/N).
 \tag{29}
\]
In fact the original packet has a sharper boundary estimate.
Let \(B\) be the branch in the complex source theorem, and put
\(L_N=(-1)^N\kappa^3e^{-3\pi i/(4N)}\). Uniformly on the same
strict compact sets,
\[
 \boxed{\quad
 \mathcal C_N(\mathbf t_{\mathbf j,N})=
 L_Ne^{i\pi/4}B(\mathbf t_{\mathbf j,N})
           e^{iN\Psi(\mathbf t_{\mathbf j,N})}(1+O(N^{-1})).
 \quad}
 \tag{30}
\]
Here the displayed \(B\) is the product
\(\prod_{i<j}(1-t_it_j)^{-1/2}\), continued radially.
There is no factor \(\prod_iD_N(t_i)\) in (30).

To prove both estimates with their normalization, use the uniform
interior sine-factorial formula
\[
 s_{Na-\gamma}=
 \sqrt N(2\sin\pi a)^{1/2-\gamma}e^{NL(a)}
                                      (1+O(N^{-1})),
 \tag{31}
\]
when the subscript is an integer, \(a\) stays in a closed
interior interval, and \(\gamma\in\{0,1/2,1\}\).
Its constant can be checked without a singular endpoint
summation. The exact identities
\(s_js_{d-j}=N\) give the middle normalization: for odd \(N\),
\(s_{d/2}=\sqrt N\); for even \(N\),
\(s_{N/2}=\sqrt{2N}\). Apply the ordinary trapezoidal
Euler--Maclaurin estimate, with error \(O(N^{-1})\), to
\(\sum\log(2\sin(\pi h/N))\) between that middle and
\(Na-\gamma\). This interval stays away from zero and one.
Since \(L(1/2)=0\), its integral and two endpoint half-weights
give exactly (31), with the stated middle constant.

In (28) the three numerator factorials have arguments
\(N(x_i+x_j)-1\), hence \(\gamma=1\). The four denominator
factorials have arguments \(Nx_i-1/2\) and \(N(S-1)-1/2\),
hence \(\gamma=1/2\). Formula (31) therefore gives
\[
 N^{3/2}T_{N,\mathbf j}
       =\prod_{i<j}(2\sin\pi(x_i+x_j))^{-1/2}
                            e^{N\tau(\mathbf x)}(1+O(N^{-1}))
       =|B(\mathbf t_{\mathbf j,N})|e^{N\tau(\mathbf x)}
                                                (1+O(N^{-1})).
 \tag{32}
\]
It also proves (29). For the phases, put
\(\Gamma_N=\prod_i\gamma_{j_i,N}
          =e^{-\pi i d(S-3/2)}\).
The radial branch has
\(\arg B=\pi S-3\pi/4\), and (8) gives
\(\operatorname{Re}\Psi=\pi(1-S)\). Direct substitution yields
\[
 \frac{L_Ne^{i\pi/4}(B/|B|)
                  e^{iN\operatorname{Re}\Psi}}{\Gamma_N}
                                          =e^{3\pi i/(4N)}.
 \tag{33}
\]
This known phase is \(1+O(N^{-1})\). Combining (27), (32),
and (33) proves (30), retaining every original scalar.
In particular the physical-grid rate is
\(2\pi\tau=2\operatorname{Vol}\).

Every coordinate in (25) has \(D_N(t_{j,N})=0\).
The full polynomial in (27) is regular there, whereas expressions
divided by the norm factors need cancellation before evaluation.
An interior asymptotic with a displayed factor \(\prod_iD_N(t_i)\)
cannot simply be evaluated on this grid.

## 5. What has been connected

Near the origin, the proved complex source connection supplies its
initialized nonzero growing packet wherever
\(\operatorname{Im}\Psi\le0\). Every compact family of the radial
paths (7) begins in that neighborhood. Theorem 2 shows that its
classical saddle height stays strictly positive for every \(r>0\);
Theorem 1 identifies its boundary height with the already constructed
ordered prism volume. Independently, (27) initializes the actual
positive source on the physical boundary grid.

These facts do not prove that the source asymptotic is transported
through the entire intervening disk, or uniformly into a
level-dependent layer approaching \(r=1\). They also do not move the
assembled Conway coefficient cycle to these local evaluations.
Estimates for that source transport and the global marked geometric
gluing are still required for arbitrary short fillings. No new
volume-identity knot family or finite-exception theorem is asserted.

## Complete proof sources and coverage

All three complete proof sources were read at their matching pins:

| Source | SHA-256 |
|---|---|
| [Centered full source compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Actual ordered ideal prisms](../papers/strict-conway-geometry/README.md) | c29321805df39a49854665df1255db1ec7180397a5dd689f19289d61335871c9 |
| [Initialized complex source connection](research_centered_tensor_complex_source_connection.md) | 9b72f6d538a828bbbf2dd0be32828a5488b91865fa93fdcedee4d0b2fb556b0c |

The complete positive Newton multiplication theorem was also read at
pin 543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb.
It already proves positivity in the full physical algebra. The new
bridge here is the exact centered unit grid, the fully normalized
boundary action, and the growing radial path for the whole strict
prism domain. No novelty is claimed for the dilogarithm Fourier
formulas, finite Fourier orthogonality, or concavity inequalities.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
