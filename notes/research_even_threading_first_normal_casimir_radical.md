# The first normal of the even encircling thread is the full Casimir radical

Private research note, 17 November 2026.

The genuine complete-color first root-normal of the even thread around
a pair is nonzero at every level, despite the zero first derivative of
each generic eigenvalue. For the specified annular cable, its actual
source-pivot correction cancels. The normal generates all double-node
radical channels, and the original Hermite closing gives an explicit
positive weighted value functional. No geometric-source comparison or
asymptotic lower bound is inferred.

## 1. The genuine pair and the fixed annular diagram

Set
\[
 q_0=e^{\pi i/N},\quad Q_0=q_0^2,\quad N\ge2,\quad D=N-1,\quad
 \delta(q)=1-q^{2N},\quad \dot A=q\,dA/dq,\quad \eta=(-1)^D.
                                                               \tag{1}
\]
Use the genuine Weyl target \(V(q)=D_D(q)\), along \(x=q^D\),
\(M=-q^N\). Its pair Casimir \(\Omega(q)\) is normalized on a highest
weight \(n\) by \(q^{n+1}+q^{-n-1}\). At the root, in the original
balanced frame, its faithful algebra is
\[
 \mathcal A_N=\mathbb C[\Omega_0]\simeq\mathbb C[C]/P_0(C),\quad
 P_0(C)=2T_N(C/2)+2=\prod_{j=0}^{D}(C-c_j),\quad
 c_j=q_0^{2j+1}+q_0^{-2j-1}.                                  \tag{2}
\]
Every distinct node is double except the odd-level simple node \(-2\).

The same pair describes one oppositely oriented physical strand.
Here is an explicit regular genuine self-duality, to distinguish it
from a generic truncated typical-color substitution. In the divided
\(F\) basis \(v_a\), with dual basis \(v^a\), put
\[
 J(q)v_a=(-1)^a q^{a(a-D-1)}
                 {D\brack a}_q\,v^{D-a}.                     \tag{3}
\]
For the conventions \(\Delta E=E\otimes K+1\otimes E\) and
\(\Delta F=F\otimes1+K^{-1}\otimes F\), substitution of
\(S(E)=-EK^{-1}\), \(S(F)=-KF\) verifies (3). Its consecutive
coefficients have ratio
\(-q^{-D+2a-2}[D-a+1]_q/[a]_q\), which verifies both \(E\) and \(F\);
\(K\) is immediate. All coefficients are nonzero at \(q_0\), since
\(a,D-a<N\). Thus \(J\) is regular and invertible near the root.
Convert (3) to the original balanced frame and normalize its harmless
scalar by the literal root cap. Conjugation by this carrier identifies
\(V\otimes V\) with \(V\otimes V^*\). At the root the latter is the
actual dual \(V(x^{-1}Q_0^{-1})\); that root parameter formula is not
asserted off root. Derivatives of this carrier will multiply a zero
zeroth defect and hence do not affect its first normal.

Take the zero-framed simple annulus encircling the two targets.
Use one auxiliary closing cut and the literal block monodromy;
with one auxiliary strand initially to the right of the targets,
its typed braid word is \([2,1,1,2]\). The \(k\) annular parallels
replace that auxiliary strand by \(k\) adjacent strands, with all
closing cuts at the same radial section. No auxiliary self-twist
or extra framing scalar is inserted. For opposite target
orientations its relative linking with the oriented core is zero.
Equivalently, after moving the auxiliary tensor factor to the first
position just for notation, put
\(A=R_{\rm aux,V}\), \(B=R_{V,\rm aux}^{21}\). The closure is
\(\operatorname{Tr}_{\rm aux}(KAB)\), and its source-adapted version
uses \(gAB\). It is not the opposite product \(BA\).

Thread this fixed diagram by
\[
 C_0=2,\qquad C_1=W,\qquad C_{n+1}=W C_n-C_{n-1},
 \qquad W=D_1(q).                                             \tag{4}
\]
All crossings are the genuine regular finite Weyl matrices.
Let \(A_K(q)\) be the degree-\(2N\) operator with ordinary auxiliary
pivot \(K=q^H\), and \(A_g(q)\) the same literal cable with each
auxiliary pivot replaced by \(g=K^{1-N}\). The latter is a specified
array lift; \(g\) is not an off-root pivotal structure. We compute
\[
             J_N=\left[\frac{A_g(q)-2I}{\delta(q)}\right]_{q_0}.
                                                               \tag{5}
\]
Original exterior data may be attached by any regular finite
contraction. Its literal mark is lifted as
\(\mathsf D(q)=g(q)^{-1}e\), \(e_{ab}=1/N\), so
\(\operatorname{Tr}(g\mathsf DT)=\operatorname{Tr}(eT)\) exactly.
The simplified root marked-cap array is not imposed independently
off root.

## 2. Literal cable fusion and the first pivot correction

For auxiliary colors \(A,B\) and target block \(V\), the two checked
braiding hexagons are
\[
\begin{split}
 c_{A\otimes B,V}
   &=(c_{A,V}\otimes I_B)(I_A\otimes c_{B,V}),\\
 c_{V,A\otimes B}
   &=(I_A\otimes c_{V,B})(c_{V,A}\otimes I_B).
\end{split}                                                   \tag{6}
\]
Starting in \(V\otimes A\otimes B\), apply the second line and then
the first: the monodromy is
\(c_{A\otimes B,V}c_{V,A\otimes B}\). This is exactly the chosen
two-parallel annular braid before closing any auxiliary index. Since
\(g_{A\otimes B}=g_A\otimes g_B\), its closure is the same finite
index sum. Iteration proves the tensor-color identity for this
fixed cable even with \(g\). No cap is slid using an off-root
\(g\)-pivotal naturality assertion.

Generic Weyl exact-sequence maps preserve \(K,H\), hence also \(g\).
The monodromy preserves their auxiliary filtration, so closing
the auxiliary index gives additivity with every target index fixed.
The integral Weyl exact sequences therefore give
\[
                 C_{2N}([W])=[D_{2N}]-[D_{2N-2}]              \tag{7}
\]
for either of these fixed trace formulas. This does not make
\(A_g\) a central Casimir polynomial off root.

For the ordinary pivot one has the full matrix identity
\[
                    A_K(q)=2T_{2N}(\Omega(q)/2).              \tag{8}
\]
To verify the normalization, the ordinary \(D_a\)-loop on a target
highest vector of weight \(n\) has highest coefficient
\[
 \sum_{b=0}^{a}q^{(n+1)(a-2b)}
       =U_a\bigl((q^{n+1}+q^{-n-1})/2\bigr).
\]
In the corresponding block-braiding order, positive nilpotent
transfers cannot return to this highest coefficient. Ordinary
pivotal covariance and the generic pair highest weights
\(2D-2j\), \(0\le j\le D\), then prove the whole operator identity.
The difference \(a=2N\) minus \(a=2N-2\) gives (8).
Regularity at the root is literal: the coefficient of
\(E^{(r)}\otimes F^{(r)}\) in the finite crossing is
\[
             q^{r(r-1)/2}\prod_{s=1}^{r}(q^s-q^{-s}).          \tag{9}
\]
The divided matrices are regular. Every \(r\ge N\) term vanishes
at \(q_0\), even if its divided matrices do not; at a crossing
with the core \(D_D\) such terms are absent. Thus this specializes
to the original restricted crossing, retaining all Jordan data.

Both auxiliary highest weights in (7) are even, so \(K^{-N}_0=I\).
Writing \(\mathcal M\) for the chosen monodromy gives
\[
\begin{split}
 (\dot g-\dot K)_0&=-N H K_0,\\
 \dot A_g(q_0)-\dot A_K(q_0)
   &=-N\,\operatorname{Tr}_{D_{2N}-D_{2N-2}}
                              (K_0H\mathcal M_0).             \tag{10}
\end{split}
\]
No monodromy derivative remains in this difference, because
\(g-K=0\) on those colors at the root.

The trace with this ONE \(H\) insertion is additive by the same
filtration argument: \(H\) preserves the submodules and quotients.
At the root (7) has class
\([\mathbb C_{2N}]+[\mathbb C_{-2N}]\). Their \(H\) values are
\(\pm2N\), ordinary pivotal dimensions are one, and double
braidings with each complete target are \(x^{\pm2N}=1\),
including a dual target. Thus the two weighted traces in (10)
are \(2NI\) and \(-2NI\):
\[
                         \dot A_g(q_0)=\dot A_K(q_0).          \tag{11}
\]
In the unfused cable each fundamental \(K^{-N}_0=-I\), and every
term of \(C_{2N}\) has an even number of strands. Differentiating
their product inserts \(-N\sum H_i\), the total \(H\) at the
common cut, which (6) carries to (10). This also checks the
literal cable signs. We have not differentiated a root-only
subquotient identity or used off-root \(g\)-pivotal naturality.

## 3. The exact first-normal polynomial and all its Jordan slopes

Let
\[
 P(q,C)=\prod_{j=0}^{D}(C-\lambda_j(q)),\qquad
 \lambda_j(q)=q^{2N-1-2j}+q^{-2N+1+2j}.                       \tag{12}
\]
This is the generic pair minimal polynomial, with \(P(q_0,C)=P_0(C)\).
It annihilates the whole pair near the root. The root middle block is
cyclic, and its cyclic-basis determinant stays nonzero near \(q_0\).

**Theorem.** The limit (5) exists and is \(r_N(\Omega_0)\), where
\[
 \boxed{\qquad
       r_N(C)=-\frac2N\,\left.\dot P(q,C)\right|_{q_0}.
 \qquad}                                                      \tag{13}
\]
This polynomial has degree at most \(N-1\). Its complete Hermite data are
\[
\begin{split}
 r_N(c_j)&=0,\\
 r_N'(c_j)&=\frac{4N(l-j)}{q_0^{2j+1}-q_0^{-2j-1}}
       =-\frac{2iN(l-j)}{\sin((2j+1)\pi/N)}
                  &&(0\le j<l=D-j),\\
 r_N(-2)&=0 &&\text{at odd levels}.
\end{split}                                                   \tag{14}
\]
Every displayed slope is nonzero. Consequently
\[
                           J_N\ne0,\qquad J_N^2=0             \tag{15}
\]
on the full physical pair, at every \(N\ge2\).

*Proof.* Put \(p(C)=2T_{2N}(C/2)-2=P_0(C)(P_0(C)-4)\) and
\(\varepsilon=\log(q/q_0)\). Since \(P(q,\Omega(q))=0\),
\[
 P_0(\Omega(q))=-\varepsilon\,\dot P(q_0,\Omega_0)
                                      +O(\varepsilon^2).
\]
Hence \(p(\Omega(q))=4\varepsilon\dot P(q_0,\Omega_0)
+O(\varepsilon^2)\). Equations (8), (11), and
\(\delta=-2N\varepsilon+O(\varepsilon^2)\) prove (13).

For a paired \(j<l=D-j\), set \(b=2j+1\), \(s=2N-b\) and
\(w=q_0^s=q_0^{-b}\). The two node velocities have sum
\[
              \dot\lambda_j+\dot\lambda_l=(s-b)(w-w^{-1}).
\]
Writing \(Q_j(C)=P_0(C)/(C-c_j)^2\), differentiation of (12) gives
\[
 \dot P(q_0,c_j)=0,\qquad
 \partial_C\dot P(q_0,c_j)
               =-(s-b)(w-w^{-1})Q_j(c_j).
\]
The elementary Chebyshev equation gives
\(Q_j(c_j)=N^2/(4-c_j^2)\). Substitution in (13) is exactly (14).
At the odd simple node the exponent in (12) is \(N\), and
\(\dot\lambda=N(q_0^N-q_0^{-N})=0\); its value is therefore zero
as well. A polynomial with these zero values has square zero
modulo \(P_0\). The nonzero slopes and faithful physical algebra
(2) prove that the operator itself is nonzero. \(\square\)

For clarity, all generic scalar eigenvalues of the defect satisfy
\[
 p(\lambda_j(q))
 =q^{2N(2N-1-2j)}+q^{-2N(2N-1-2j)}-2
 =O(\varepsilon^2).
\]
But a colliding pair has
\(\lambda_j-\lambda_l=2N(w-w^{-1})\varepsilon
+O(\varepsilon^2)\). Its divided difference is only first order.
This is precisely the nilpotent term (14) that a calculation of
eigenvalue derivatives alone misses.

There is also an exact identification with an already existing
original crossing operator. Write
\(R=\kappa u_N(\Omega_0)\), \(\kappa=q_0^{D^2/2}\), with the
original Cartan half-character. The complete crossing-circle source
gives, at every double node,
\[
 u_N(c_j)=(-1)^j q_0^{j(j+1)},\qquad
 \frac{u_N'(c_j)}{u_N(c_j)}
       =-\frac{D-2j}{2(q_0^{2j+1}-q_0^{-2j-1})}.
\]
Consequently \(u_N^{2N}\) has value one at every node, including
the odd simple node, and slope
\(-N(D-2j)/(q_0^{2j+1}-q_0^{-2j-1})\). Comparison with (14)
in the full Hermite algebra proves
\[
 \boxed{\quad
 r_N=4(1-u_N^{2N}),\qquad
 J_N=4(I-\kappa^{-2N}R^{2N})=4(I-\eta R^{2N}).
 \quad}                                                       \tag{15a}
\]
Here \(\kappa^{2N}=(-1)^{D^2}=\eta\). Thus the normal is the
unipotent part of a specified level-dependent original crossing
power. The theorem identifies its first-thread-normal origin;
it does not add an independent fixed-root source generator.

## 4. The prescribed closing becomes a positive value functional

Retain the original Hermite source functional, with no extra
normalization:
\[
 \phi(f)=\frac1N\operatorname{Tr}[(I\otimes g_0)f(\Omega_0)]
 =\eta\sum_{c\ {\rm double}}\bigl((4-c^2)f'(c)-cf(c)\bigr)
       +\mathbf1_{N\ {\rm odd}}f(-2).                         \tag{16}
\]
At an opposite-oriented port transport this functional by the same
carrier (3) and the original turns; no independent turn scalar is
introduced.
For every \(f\in\mathcal A_N\),
\[
 \boxed{\quad
 \phi(r_N f)=-8i\eta N
      \sum_{0\le j<D-j}(D-2j)\sin((2j+1)\pi/N)\,f(c_j).
 \quad}                                                       \tag{17}
\]
All weights are strictly positive real numbers after removal of
the one common phase. In particular
\[
                       \phi(r_N)
                    =-\frac{4i\eta N^2}{\sin(\pi/N)}\ne0.     \tag{18}
\]
One direct check is the leading coefficient. From
\(\sum_j\lambda_j(q)=[2N]_q\) and (13),
\[
 [C^{N-1}]r_N(C)=\frac8{q_0-q_0^{-1}}.
\]
The original endpoint identity
\(\phi(f)=\eta N^2[C^{N-1}](f\bmod P_0)\) proves (18).
Equivalently differentiating the finite geometric sum gives
\[
 \sum_{j=0}^{N-1}(D-2j)e^{i(2j+1)\pi/N}
                              =\frac{iN}{\sin(\pi/N)};
\]
paired terms have equal imaginary parts and the odd center has
zero coefficient, giving the positive sum in (17).

Multiplication by \(r_N\) identifies the value algebra on the
double nodes with the entire square-zero radical of \(\mathcal A_N\):
it sends \(f(c_j)\) to the slope \(r_N'(c_j)f(c_j)\), and every
\(r_N'(c_j)\) is a unit. It kills all derivative inputs and the
odd simple component. For coefficient conjugation \(f^\sharp\),
\[
 \frac{i\eta}{8N}\phi(r_N f^\sharp f)
       =\sum_{j<D-j}(D-2j)\sin((2j+1)\pi/N)|f(c_j)|^2.         \tag{19}
\]
This positive functional has a specified first-normal origin.
It is not a replacement for the original indefinite derivative closing.
In fact its quadratic form is zero on \(f=r_N\) itself, while
\(\phi(r_N)\ne0\) by (18). Thus this value-only positive form cannot
control the full original closing, even on its own normal generator.

There is a sharp further limitation under an actual permissible
turn. For the unscaled original quarter-turn \(\mathcal R\),
the literal rotation and cup identities in the pair source give
\(\phi(\mathcal R f)=f(c_0)\). Here put \(x=q_0^D\).
For completeness, substituting
\(\mathcal R(B)_{(a,b);(c,e)}
=x^{a-e}B_{(b,D-e);(D-a,c)}\) in (16), using
\(g_b=x^{-D}Q_0^{-b}=x^{2b-D}\), reduces the trace to
\[
 \frac1N\sum_{a,b=0}^{D}
       x^{a+b-D}B_{(b,D-b);(D-a,a)}.
\]
The original cup is proportional to the vector with middle-block
entries \(x^b\); \(B=f(\Omega_0)\) is symmetric and acts on that cup
by \(f(c_0)\). The displayed sum is therefore \(f(c_0)\).
In particular
\[
                \phi\bigl(\mathcal R(r_N f)\bigr)=0
                       \quad\text{for every }f\in\mathcal A_N. \tag{19a}
\]
Thus one original turn followed by the prescribed closing kills
this entire locally detected normal family. No transported
noncancellation follows from (18).

For any regular finite original exterior contraction \(\mathcal L(q)\),
\[
 \left[\frac{\mathcal L(q)[A_g(q)-2I]}{\delta(q)}\right]_{q_0}
                          =\mathcal L(q_0)[r_N(\Omega_0)].    \tag{20}
\]
All derivatives of its mark, turns, basis carriers, coupons and
framing factors multiply the zeroth defect and vanish. Thus
(16)--(18) retain the actual root Hermite observation rather than
an ordinary trace on the pair. An arbitrary exterior can still
annihilate \(r_N\); no particular knot scalar or geometric coefficient
is asserted to survive.

The opposite-oriented pair has relative linking zero, so this
already disproves universal entrywise first-\(q\)-normal vanishing
on the genuine Weyl path \(M=-q^N\). It does not contradict the
vanishing of all fixed-root meridian jets. The annular framing and
cable placement in Section 1 are part of the theorem; arbitrary
off-root changes of these data are not identified.

## Complete direct sources

All four texts were read completely for this proof.

1. [The actual ADO threaded character](ado_threaded_shadow.md),
   SHA256 \(\texttt{c97b10ee6fa4d629e5f5e21297eec78acf236a7f136628b1153e97b413b6910d}\).
   Integral Weyl identities, root auxiliary filtration and even colors.
2. [The exact Weyl-normal insertion](research_even_threading_weyl_normal_source.md),
   SHA256 \(\texttt{8a9c6e449fb5536d7a44f329e2f37afae172cce2812838cf5d3de22959667f21}\).
   Genuine regular source lift, high divided-power coefficients,
   corrected mark and exterior localization.
3. [Original crossing-circle sources](actual_crossing_circle_source_and_filling.md),
   SHA256 \(\texttt{302db6493c53f8c5267e4753eca2c2de89d67df7365eb9530baeb17194ccf0d0}\).
   Literal annular braid and ordinary-pivot Casimir normalization.
4. [The full physical pair commutant](actual_pair_casimir_commutant_and_rotated_trace.md),
   SHA256 \(\texttt{00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666}\).
   Faithful full Hermite algebra, generic spectrum and original \(\phi\).

Only written finite-dimensional proofs were used. No mathematical
program, numerical test or build was run.

