# Exact endpoint conditions for the full outer adjoint

Private full-algebra proof, 8 November 2026. The transpose of the
original seven-term operator need not preserve the outer radical.
Its failure is confined to three central physical values, with
different double/simple bookkeeping at the two parities. Three
explicit test values remove it exactly. No derivative of the test
function is involved.

This note gives the full endpoint map and its original trace
pairing. It makes no inverse, endpoint-smallness, or outer
cancellation assertion. No mathematical numerical evaluation or
frozen-source edit is used.

## 1. Original algebra, transpose, and radical test

Use the notation and full Frobenius pairing of
[the seven-term recurrence](research_mixed_next_physical_inner_seven_term_recurrence.md):
\[
\begin{gathered}
N\ge6,\quad m=\lfloor N/2\rfloor\ge3,\quad
D=N-1,\quad U=m-1,\quad M=\lceil N/2\rceil,\\
\theta=\pi/N,\quad q=e^{i\theta},\quad\eta=(-1)^D,\quad
\mathcal A_N=\mathbb C[z]/(P_N),\quad P_N=2T_N(z/2)+2,\\
c_j=2\cos((2j+1)\theta),\quad
t_j=\pi-(2j+1)\theta,\quad c_j=-2\cos t_j,\\
\mathcal L=TZT,\qquad
\mathcal L_n=R^{-n}\mathcal L R^n .
\end{gathered}                                                     \tag{1}
\]
The double nodes have \(0\le j\le U\). At odd levels there
is also the simple node \(c_m=-2\), \(t_m=0\).
The first even level covered is six, and the first odd level
covered is seven. Smaller levels are not classified here.

The original \(T,\mathcal L,Z\), and multiplication by \(R\)
are self-adjoint for the bilinear Frobenius pairing. Therefore
\(\mathcal L_n^{\mathrm t}=\mathcal L_{-n}\), without conjugating
any scalar. The exact transpose of the recurrence operator is
\[
\boxed{\quad
\mathcal D_3^{\mathrm t}
 =q^{-2}\mathcal L_{-1}(\mathcal L^2-I)
   +q^{-3}Z\mathcal L-8q^{-2}\mathcal L
                      +(8q^{-1}+2)I
 =TR^{-3}(\mathcal L+2)R^3T .
\quad}                                                            \tag{2}
\]
In particular the order in the first product and in \(Z\mathcal L\)
is retained.

The physical radical is
\[
\mathfrak r_N=e_M\mathcal A_N,\qquad \mathfrak r_N^2=0.
                                                                    \tag{3}
\]
This is the original ideal of elements vanishing at every distinct
physical node, including the odd simple node; see
[radical contraction, Section 1](research_high_newton_radical_contraction.md).
For an arbitrary \(h\in\mathcal A_N\), put
\[
g=R^3e_Mh,\qquad
p_j=\left.\partial_t g(-2\cos t)\right|_{t=t_j}
   =2\sin t_j\,R(c_j)^3e_M'(c_j)h(c_j).
                                                                    \tag{4}
\]
All \(g(c_j)\) vanish, and at odd levels \(g(-2)=0\).
Every multiplier of \(h(c_j)\) in (4) is nonzero. In
particular \(g\) depends only on the values \(h(c_j)\) at
the double nodes, not on their first normals or on \(h(-2)\).

## 2. A complete grouped-jet realization

Here are exact formulas specifying every entry of the endpoint
map, including its non-leading entries. They also verify that
no higher normal is hidden in a coalescing limit.

For any original polynomial \(f\), write
\[
v_j=f(c_j),\qquad
p_j=\left.\partial_t f(-2\cos t)\right|_{t=t_j}
              =2\sin t_j f'(c_j).
                                                                    \tag{5}
\]
Only the value \(v_m=f(-2)\) is specified at the odd simple
node; its angular derivative is identically zero.
Use the original angular functions
\[
\begin{gathered}
A(t)=\frac{4\cos^4((t-\theta)/2)}
                  {\sin t\sin(t-\theta)},\qquad C(t)=A(-t),\\
B(t)=c_0+A(t)+C(t),\qquad
a_n(t)=q^ne^{-int}A(t),\qquad
c_n(t)=q^ne^{int}C(t).
\end{gathered}                                                     \tag{6}
\]
At each regular double node the value and angular derivative
of \(\mathcal L_n f\) are
\[
\begin{split}
v_j^{(n)}
 &=B_jv_j-a_{n,j}v_{j+1}-c_{n,j}v_{j-1},\\
p_j^{(n)}
 &=B_j'v_j+B_jp_j
       -a_{n,j}'v_{j+1}-a_{n,j}p_{j+1}
       -c_{n,j}'v_{j-1}-c_{n,j}p_{j-1}.
\end{split}                                                       \tag{7}
\]
Here a prime on a coefficient means angular differentiation.
At the far node \(j=0\), omit the two \(c_{n,0}\) terms:
both \(c_n(t_0)\) and \(c_n'(t_0)\) are zero. Indeed the
original outward coefficient has a cubic zero at
\(t_0=\pi-\theta\). At the last odd double node \(j=U\),
formula (7) holds with \(v_{U+1}=v_m\), \(p_{U+1}=0\).

For the even coalescing node \(t_U=\theta\), put
\[
a_{-1}=\frac4{\sin\theta},\qquad
a_0=-\frac{4\cos\theta}{\sin^2\theta},\qquad C_*=C(\theta).
                                                                    \tag{8}
\]
The subscript on \(a_{-1}\) in (8) is a Laurent coefficient,
not the crossing index in \(a_n(t)\). The exact grouped values are
\[
\begin{split}
v_U^{(n)}
={}&c_0v_U+C_*(v_U-q^{2n}v_{U-1})
                  +a_{-1}(2p_U+in v_U),\\
p_U^{(n)}
={}&c_0p_U+C'(\theta)(v_U-q^{2n}v_{U-1})\\
 &+C_*\{p_U-q^{2n}(p_{U-1}+in v_{U-1})\}\\
 &+a_0(2p_U+in v_U)
                 +a_{-1}(-in p_U+n^2v_U/2).
\end{split}                                                       \tag{9}
\]
To prove (9), write \(t=\theta+\delta\). Evenness gives
\(f(-2\cos(t-2\theta))=f(-2\cos(\theta-\delta))\).
The singular difference in the \(A\)-term is
\[
 f(-2\cos(\theta+\delta))
 -e^{-in\delta}f(-2\cos(\theta-\delta))
 =(2p_U+in v_U)\delta
       +(-in p_U+n^2v_U/2)\delta^2+O(\delta^3).
                                                                    \tag{10}
\]
The original \(A(\theta+\delta)=a_{-1}/\delta+a_0+O(\delta)\).
Multiplication proves (9). In particular the second derivative
of the input cancels from the required first normal.

At the odd simple node \(t_m=0\), instead set
\[
\begin{split}
\alpha_{-1}&=-\frac{4\cos^4(\theta/2)}{\sin\theta},\\
\alpha_0&=-\frac{8\cos^3(\theta/2)\sin(\theta/2)}{\sin\theta}
          -\frac{4\cos^4(\theta/2)\cos\theta}{\sin^2\theta}.
\end{split}                                                       \tag{11}
\]
The sole required output there is
\[
v_m^{(n)}
 =(c_0+2\alpha_0)v_m-2q^n\alpha_0v_U
                         +2q^n\alpha_{-1}(p_U+in v_U).
                                                                    \tag{12}
\]
Indeed \(A(t)=\alpha_{-1}/t+\alpha_0+O(t)\) and
\(C(t)=-\alpha_{-1}/t+\alpha_0+O(t)\). Expanding the
two shifted values at \(2\theta\), with their exact
\(q^ne^{\pm int}\) factors, proves (12). No spectral
derivative at the simple node is prescribed.

Let \(\mathbb J_n\) denote the finite jet map (7),(9) or
(7),(12), and let \(\mathbb Z\) denote multiplication by \(z\):
\[
(v_j,p_j)\longmapsto
  (c_jv_j,\;2\sin t_j\,v_j+c_jp_j),\qquad
 v_m\longmapsto-2v_m\quad\hbox{at odd levels}.
                                                                    \tag{13}
\]
The exact full endpoint map used below is the value component of
\[
\boxed{\quad
q^{-2}\mathbb J_{-1}(\mathbb J_0^2-I)
  +q^{-3}\mathbb Z\mathbb J_0-8q^{-2}\mathbb J_0
                              +(8q^{-1}+2)I
\quad}                                                            \tag{14}
\]
on the input \((v_j=0,p_j)\) from (4), with \(v_m=0\) when
odd. Equations (6)--(14) specify the entire matrix with no
ungrouped singular coefficient or omitted normal.

## 3. Localization and the exact vanishing conditions

For a radical input, (7),(9),(12) show immediately that
the only first-step nonzero physical value is
\[
\begin{array}{ll}
N\text{ even}:&
 (\mathcal L_n g)(c_U)=\displaystyle\frac8{\sin\theta}p_U
                                   =16g'(c_U),\\[2mm]
N\text{ odd}:&
 (\mathcal L_n g)(-2)
 =\displaystyle-\frac{8q^n\cos^4(\theta/2)}{\sin\theta}p_U
 =-32q^n\cos^4(\theta/2)\cos\theta\,g'(c_U).
\end{array}                                                       \tag{15}
\]
Every other physical value is zero. Write
\[
\beta=\frac8{\sin\theta},\qquad
\gamma=-\frac{8\cos^4(\theta/2)}{\sin\theta},\qquad
b_j=(\mathcal D_3^{\mathrm t}g)(c_j).
                                                                    \tag{16}
\]
The full jet maps are nearest-neighbor maps, including (9),(12).
Consequently (14),(15) imply
\[
\begin{array}{ll}
N\text{ even}:& b_j=0\quad(j\notin\{U-2,U-1,U\}),\\
N\text{ odd}:& b_j=0\quad(j\notin\{U-1,U,m\}).
\end{array}                                                       \tag{17}
\]
Each possibly nonzero value is a linear combination only of
\(p_U,p_{U-1},p_{U-2}\).
There is no additional far-end condition: the cubic zero
used in (7) holds for the full first-normal data as well.

The following triangular formulas prove the exact rank of
this endpoint obstruction. Here \(A_j=A(t_j)\) and
\(C_j=C(t_j)\), at the displayed regular occurrences.

At even levels,
\[
\begin{split}
b_{U-2}
 &=q^{-3}e^{it_{U-2}}A_{U-2}A_{U-1}\,\beta p_U,\\
b_{U-1}\big|_{p_U=0}
 &=q^{-3}e^{it_{U-1}}A_{U-1}C_U\,\beta p_{U-1},\\
b_U\big|_{p_U=p_{U-1}=0}
 &=q^{-2}C_UC_{U-1}\,\beta p_{U-2}.
\end{split}                                                       \tag{18}
\]
At odd levels,
\[
\begin{split}
b_{U-1}
 &=q^{-3}e^{it_{U-1}}A_{U-1}A_U\,\gamma p_U,\\
b_U\big|_{p_U=0}
 &=q^{-3}e^{it_U}A_UC_U\,\gamma p_{U-1},\\
b_m\big|_{p_U=p_{U-1}=0}
 &=q^{-3}C_UC_{U-1}\,\gamma p_{U-2}.
\end{split}                                                       \tag{19}
\]
All displayed coefficients are nonzero for \(m\ge3\).
Their sine denominators are regular in these ranges, and
the phases and \(\beta,\gamma\) are nonzero.

For clarity, the first equation in either table comes solely
from the outermost propagation of the first-step value in
\(q^{-2}\mathcal L_{-1}\mathcal L^2g\). If \(p_U=0\),
then \(\mathcal Lg\) is again radical and its last angular
normal is \(-C_Up_{U-1}\). Apply (15) once more and
the next regular shift to obtain the second equation.
If also \(p_{U-1}=0\), then \(\mathcal L^2g\) is radical,
with last angular normal \(C_UC_{U-1}p_{U-2}\); applying
\(\mathcal L_{-1}\) gives the third equation. All lower
terms in (2) vanish at the relevant output under these
successive conditions. This proves the tables without
dropping any non-leading endpoint coefficient; those
coefficients remain exactly specified by (14).

**Theorem.** For \(m\ge3\),
\[
\boxed{\quad
\mathcal D_3^{\mathrm t}(R^3e_Mh)\in\mathfrak r_N
\quad\Longleftrightarrow\quad
h(c_U)=h(c_{U-1})=h(c_{U-2})=0.
\quad}                                                            \tag{20}
\]
Sufficiency follows from the localized map (14),(17).
Necessity follows successively from (18) or (19) and the
nonzero multipliers in (4).
These are three value conditions; imposing first derivatives
of \(h\) to vanish is unnecessary.

At odd levels a slightly weaker statement is useful.
Vanishing of every double-node value of
\(\mathcal D_3^{\mathrm t}g\), and hence of every newly
introduced first-normal coefficient in its trace pairing,
is equivalent to \(h(c_U)=h(c_{U-1})=0\).
The remaining simple-node value is then precisely the
last line of (19), and vanishes only with the third condition.
It may instead be retained explicitly.

## 4. The exact full pairing and its surviving endpoint terms

Let \(E_j\) be the canonical full Hermite idempotent with
value one at \(c_j\), zero at every other distinct node,
and zero first spectral derivative at every double node.
At odd levels include the simple idempotent \(E_m\).
Subtracting \(\sum b_jE_j\) from \(\mathcal D_3^{\mathrm t}g\)
leaves a radical. Thus there is a unique list of double-node
values \(\widehat h_j\) such that
\[
\mathcal D_3^{\mathrm t}g
 =R^3e_M\widehat h+\sum_{j=0}^{U}b_jE_j
                         +{\bf1}_{N\ {\rm odd}}b_mE_m.
                                                                    \tag{21}
\]
One may take \(\widehat h\) of degree at most \(U\).
Its values are explicitly
\[
\widehat h_j=
 \frac{(\mathcal D_3^{\mathrm t}g)'(c_j)}
             {R(c_j)^3e_M'(c_j)}.
                                                                    \tag{22}
\]
The numerators, including all their coalescing first normals,
are supplied by (14). The derivatives of the idempotents
in (21) are zero by definition.

Keep exactly the original consumed-normal weights
\[
\mu_{j,N}
 =\eta(4-c_j^2)R(c_j)^3e_M'(c_j)
 =\beta_{j,N}R(c_j)^3.
                                                                    \tag{23}
\]
The local full trace formula of the radical source gives,
for every \(F\in\mathcal A_N\),
\[
\boxed{\begin{split}
\phi_N((\mathcal D_3^{\mathrm t}g)F)
={}&\sum_{j=0}^{U}\mu_{j,N}\widehat h_j F(c_j)\\
 &+\eta\sum_{j\in\mathcal C_N}
   b_j\{(4-c_j^2)F'(c_j)-c_jF(c_j)\}\\
 &+{\bf1}_{N\ {\rm odd}}b_m F(-2),
\end{split}}                                                      \tag{24}
\]
where
\[
\mathcal C_N=
\begin{cases}
\{U-2,U-1,U\},&N\text{ even},\\
\{U-1,U\},&N\text{ odd}.
\end{cases}
                                                                    \tag{25}
\]
In particular the coefficient of each newly exposed first
normal is exactly
\(\eta(4-c_j^2)(\mathcal D_3^{\mathrm t}g)(c_j)\).
The odd simple-node term in (24) is a value term, not a
surrogate normal.

Apply this to the original full output \(Q_N^{\rm full}\)
of the seven-term theorem, which satisfies
\(\mathcal D_3Q_N^{\rm full}=\mathfrak f_N1\).
The exact global identity is
\[
\begin{split}
\sum_{j=0}^{U}\mu_{j,N}\widehat h_j q_{j,N}
={}&\mathfrak f_N\sum_{j=0}^{U}\mu_{j,N}h(c_j)\\
 &-\eta\sum_{j\in\mathcal C_N}
 b_j\{(4-c_j^2)(Q_N^{\rm full})'(c_j)-c_jq_{j,N}\}\\
 &-{\bf1}_{N\ {\rm odd}}b_mQ_N^{\rm full}(-2).
\end{split}                                                       \tag{26}
\]
The even forcing \(4\kappa^3/N^2\) and odd zero forcing
are unchanged. In the regular interior, (22) agrees with
the weighted sequence adjoint from the recurrence theorem;
(24)--(26) supply its missing endpoint completion.

Only the double-node values \(q_{j,N}\) may be identified
with the shortened physical output. The first normals
in (26), and the odd simple-node value, are those of
the full output explicitly displayed there. No equality
with the shortened polynomial's first normals or its
simple-node value has been used.

If (20) holds, every endpoint defect in (24)--(26) vanishes
exactly. This does not prove that a prescribed observation
can be obtained as \(\widehat h\) under those three conditions,
or bound an inverse on that constrained test space.
Without those conditions the same identities retain the
complete three-dimensional endpoint obstruction. No
estimate of its exponential size is asserted.
