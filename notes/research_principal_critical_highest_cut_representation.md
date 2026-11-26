# The principal critical point with its original highest cut

Private written proof, 18 November 2026.

The convergent principal phase of [A] has a direct map to an
irreducible local knot representation. The map is obtained from the
literal coherent crossing kernels in regular creation and momentum
fields. It remains defined when occupation coordinates vanish.
The highest cut is closed by conserved triangular matrix products,
not replaced by the averaged cut used in [M, Section 6].

This identifies a classical critical point and its actual mark
observables. It does not identify the analytic quantum minor with
that stationary sector, identify a longitude with an action
derivative, or select the hyperbolic component or a physical cycle.

## 1. Source and assertion

Use exactly the one-component braid, natural meridian \(Y=x_0^2\),
and simple two-branch hypotheses of [A]. Write \(z=Y-\alpha\), with
\(\alpha\ne0,1\), and retain
\[
 T_0=\operatorname{diag}(0,1,\ldots,1),\qquad
 L=L_\beta(x_0),\qquad B=LT_0.
 \tag{1}
\]
Choose the holomorphic square root \(x_0\) on the meridian disk.
The source of [A] supplies an analytic relative-word principal
phase \(\mathcal P(z,Z,P,\mathbf t)\), quartic in the fields at
zero marks, and
\[
 C=B(I-B)^{-1}=\frac{uv^T}{z}+G(z),\qquad uv^T\ne0.
 \tag{2}
\]
The vectors \(u,v\) are fixed residue factors; \(G\) is holomorphic.
No normalization \(v^Tu=1\) is imposed.

Its hard effective phase is \(\Psi(z,x,\mathbf t)\), where
\(x=AB_s\) is the product of the two soft fields. At zero marks,
\[
 \Phi(z,x)=-zx+\Psi(z,x,0),\qquad
 x_g(z)=\frac{z}{2\sigma}+O(z^2),\quad \sigma\ne0,\qquad
 \Psi_x(z,x_g(z),0)=z.
 \tag{3}
\]
These are the convergent functions proved in [A], not a new
stationary ansatz.

**Assertion.** For sufficiently small \(z\ne0\), the critical point
(3), with the original highest-cut conditions, gives an irreducible
\(\mathrm{SL}_2(\mathbb C)\) representation of the original braid
closure. A representative is holomorphic in \(\sqrt z\); its
character is holomorphic in \(z\) and limits to the abelian
character at \(z=0\). The actual leading clock map of [A] is the
vector of stage occupations at this point, with the same fixed
linear specialization for matching-lattice clocks.

All statements about knot representations below are at zero stage
marks. The marks are retained as independent source deformations
and differentiated there. Arbitrary nonzero stage marks can insert
additional jumps and are not asserted to describe ordinary knot
representations.

## 2. A field chart without occupation denominators

For one strand use creation and momentum fields \((Z,P)\). Put
\[
 t=ZP,\qquad
 K=x_0e^{-t},\qquad f=Z,\qquad e=P\varphi_Y(t),
 \quad
 \varphi_Y(t)=\frac{(1-e^t)(1-Ye^{-t})}{x_0t}.
 \tag{4}
\]
The quotient has its holomorphic value
\(\varphi_Y(0)=x_0-x_0^{-1}\), a unit near \(Y=\alpha\).
Consequently (4) is regular even when \(Z\) or \(P\) is zero, and
\[
                  K+K^{-1}+ef=x_0+x_0^{-1}.
 \tag{5}
\]
It is a local chart on this Casimir surface at \((x_0,0,0)\).
Indeed \(ef=t\varphi_Y(t)\) has nonzero derivative at \(t=0\);
solve for \(t\), then set \(Z=f\) and \(P=e/\varphi_Y(t)\).
Equation (5) determines the unique nearby \(K\), since
\(1-x_0^{-2}\ne0\).

This chart is the regular field version of [M, (4.1)]:
with \(A=e^t\), its product is
\(ef=(1-A)(1-Y/A)/x_0\).
No logarithm of \(Z\), \(P\), \(e\), or \(f\) has been chosen.

We use a type-two generating function \(\mathcal S(Z,p)\):
its input position is \(q=\partial_p\mathcal S\), its output
momentum is \(P'=\partial_Z\mathcal S\), and its output position
is \(Z\). The mixed Hessian of each crossing is invertible near
zero, since its constant part is the invertible matrix \(L_\pm\).
Thus the analytic functions constructed in [A] give actual local
canonical maps.

For the positive crossing, let \(N,C_0,B_0\) be the analytic
implicit variables of [A, (10), (15), (17)]. Its three means are
\[
 U=(1-Y^{-1})Z_1p_1,\qquad
 V=x_0^{-1}Z_2p_1,\qquad W=x_0^{-1}Z_1p_2.
 \tag{6}
\]
The full kernel phase is \(U+V+W+F_{\rm Pois}(U,V,W)\).
The Poisson identity gives its derivatives with respect to these
means as \(N/U,C_0/V,B_0/W\), interpreted as analytic units.
On a dense open set, therefore,
\[
 q_1=\frac{N+C_0}{p_1},\quad q_2=\frac{B_0}{p_2},
 \qquad
 P'_1=\frac{N+B_0}{Z_1},\quad P'_2=\frac{C_0}{Z_2}.
 \tag{7}
\]
These quotient expressions are only a calculation on that set;
the derivatives defining the canonical map are holomorphic.
The input occupations are \(N+C_0,B_0\), and the output
occupations are \(N+B_0,C_0\).

Write \(s=N+C_0\). Exponentiating the derivatives of the literal
potential [A, (15)] gives
\[
\begin{split}
 B_0&=x_0^{-1}Z_1p_2e^{C_0},\\
 e^N-1&=Z_1p_1\,\frac{e^s-1}{s}(1-e^s/Y),\\
 (e^{C_0}-1)(1-e^{C_0}/Y)
   &=x_0^{-1}Z_2p_1e^{B_0}\frac{e^s-1}{s}(1-e^s/Y).
\end{split}
 \tag{8}
\]
For example the second identity follows from the \(N\) equation
by canceling its factor \(N\); the resulting identity extends to
\(N=0\). The first and second lines imply
\[
 Z_1=K_1e^N f_2,\qquad
 e^N-1=(e^s/x_0)Z_1e_1,\qquad
                 e^N(1-e_1f_2)=1.
 \tag{9}
\]
The last line of (8) gives \(e'_2=e_1e^{B_0+N}/x_0\).
Thus, with \(d=1-e_1f_2\), four output fields are exactly
\[
 K'_1=K_2d,\quad K'_2=K_1/d,\quad
 f'_1=K_1f_2/d,\quad e'_2=e_1/(K_2d).
 \tag{10}
\]
Both output Casimirs equal (5). Solving them on the dense set
where the remaining division is allowed gives
\[
 e'_1=\frac{de_2+e_1(dK_2-K_2^{-1})}{K_1},\qquad
 f'_2=K_2\{df_1+f_2(d/K_1-K_1)\}.
 \tag{11}
\]
Every denominator in (10)--(11) is a unit on a sufficiently
small field polydisk. Hence these identities hold throughout
that disk, including all zero field coordinates. They are exactly
the Gauss map [M, (4.6)], now derived from the analytic kernel.

The negative crossing can be checked directly as well. Use the
implicit variables \(N,C_0,A_0\) and potential [A, (16)], with
means \((1-Y)Z_2p_2,x_0Z_1p_2,x_0Z_2p_1\).
Its input occupations are \(A_0,N+C_0\), and its output
occupations are \(C_0,N+A_0\). The corresponding three equations
give, with \(s=N+C_0\),
\[
\begin{split}
 A_0&=x_0Z_2p_1e^{-s},\\
 e^N-1&=Z_2p_2e^{-A_0}
                         \frac{e^s-1}{s}(1-Ye^{-s}),\\
 (e^{C_0}-1)(1-Ye^{-C_0})
   &=x_0Z_1p_2e^{-A_0}
                         \frac{e^s-1}{s}(1-Ye^{-s}).
\end{split}
 \tag{12}
\]
It follows that \(c=1-(K_1/K_2)e_2f_1=e^N\) and
\[
\begin{split}
 K'_1&=K_2c,& K'_2&=K_1/c,&
 e'_1&=K_1e_2,& f'_2&=f_1/K_2,\\
 f'_1&=f_1+f_2/K_1-f_1/(K_2^2c),&&
 e'_2=K_2e_1+e_2-K_1^2e_2/c .
\end{split}
 \tag{13}
\]
The last two identities again follow from the Casimirs and extend
holomorphically. Direct substitution in (10)--(11) shows that
(13) is their inverse. Thus the two signed kernel maps are
analytic inverses. No inference from a merely formal inverse
or from dimension equality is needed.

## 3. Reconstructing the full coherent critical point

At zero marks the full-word kernel has principal generating
function
\[
             \mathcal S(Z,p)=Z^TLp+\mathcal P(z,Z,Lp,0).
 \tag{14}
\]
Finite composition in [A, (25)--(26)] is elimination by the
stationary equations of the intermediate coherent fields.
Differentiating those displayed equations verifies the type-two
matching convention used above. In particular (14) is the
composition of the literal signed canonical maps, in the original
word order.

Set \(P=Lp\), and abbreviate derivatives of \(\mathcal P\) by
\(\mathcal P_Z,\mathcal P_P\). The highest vector at the input
sets \(p_1=0\); the highest covector at the output sets \(Z_1=0\).
The trace closes both fields on every other strand. Since
\[
              q=L^T(Z+\mathcal P_P),\qquad
              P'=P+\mathcal P_Z,
\]
these conditions are exactly
\[
 p=T_0(P+\mathcal P_Z),\qquad
 Z=T_0L^T(Z+\mathcal P_P).
 \tag{15}
\]
Multiplying the first equation by \(L\), they become
\[
 P=B(P+\mathcal P_Z),\qquad Z=B^T(Z+\mathcal P_P).
 \tag{16}
\]
For \(z\ne0\), (16) is equivalently
\[
                    P=C\mathcal P_Z,\qquad
                    Z=C^T\mathcal P_P .
 \tag{17}
\]
Only \(I-B\) is inverted here; \(T_0\) is not.

The hard implicit equations of [A, (23), (28)--(29)] are
\[
 Z=vA+G^T\mathcal P_P,\qquad
 P=uB_s+G\mathcal P_Z .
 \tag{18}
\]
The hard envelope identity gives
\[
             \Psi_A=v^T\mathcal P_Z,\qquad
             \Psi_{B_s}=u^T\mathcal P_P.
 \tag{19}
\]
Because \(\Psi=\Psi(z,AB_s,0)\), the critical equation
\(\Psi_x=z\) with \(AB_s=x_g(z)\ne0\) implies
\[
                v^T\mathcal P_Z=zB_s,\qquad
                u^T\mathcal P_P=zA .
 \tag{20}
\]
Substitution of (20) in (18), using (2), proves (17).
Thus this analytic critical point satisfies every original
coherent matching equation and both original cut vacua.

Choose \(A=B_s=\sqrt{x_g(z)}\). Since \(\mathcal P\) is quartic,
the unique hard solution has
\[
 Z=v\sqrt{x_g}+O(x_g^{3/2}),\qquad
 P=u\sqrt{x_g}+O(x_g^{3/2}).
 \tag{21}
\]
Both field vectors are nonzero for all sufficiently small
\(z\ne0\). All intermediate fields are holomorphic and small,
by the finite local canonical composition. The original pivot
and scalar framing have no principal term by [A, Section 4];
they are not removed from the quantum source.

## 4. The cut closes by exact triangular conservation

Define
\[
 b_+(K,e)=\begin{pmatrix}K&e\\0&1\end{pmatrix},
 \qquad
 b_-(K,f)=\begin{pmatrix}1&0\\-Kf&K\end{pmatrix},
 \qquad
 G_0=b_-^{-1}b_+
      =\begin{pmatrix}K&e\\Kf&K^{-1}+ef\end{pmatrix}.
 \tag{22}
\]
These matrices are invertible throughout our field chart.
Substitution of (10)--(11) gives
\[
 b'_{+,2}b'_{+,1}=b_{+,2}b_{+,1},\qquad
 b'_{-,2}b'_{-,1}=b_{-,2}b_{-,1},\qquad
 b'_{+,2}b'_{-,1}=b_{-,2}b_{+,1}.
 \tag{23}
\]
For example the upper-right entry in the first identity is
\((K_1/d)e'_1+e_1/(K_2d)=K_2e_1+e_2\); the lower-left
identity is the same substitution with \(f\). In the third,
the entries are \(K_1,e_1,-K_1K_2f_2,K_2d\) on both sides.
The inverse map preserves the same two ordered products.
Hence every signed word conserves
\(b_{\pm,b}\cdots b_{\pm,1}\), in that order.

Equation (15) makes the input and output fields identical on
strands \(2,\ldots,b\). At the cut, \(p_1=0\) gives
\[
 e_{\mathrm{in},1}=0,\quad K_{\mathrm{in},1}=x_0,
\]
and \(Z_1=0\) gives
\[
 f_{\mathrm{out},1}=0,\quad K_{\mathrm{out},1}=x_0.
 \tag{24}
\]
Cancel the identical invertible factors for strands \(b,\ldots,2\)
from each conserved product. This proves
\(b_{\pm,1}^{\mathrm{out}}=b_{\pm,1}^{\mathrm{in}}\).
It forces \(f_{\mathrm{in},1}=e_{\mathrm{out},1}=0\) as well.
Since \(\varphi_Y\) is a unit, the cut creation and momentum
fields now both close, with both equal to zero.
This is the required highest-cut adapter. It uses neither
scalarity of the cut matrix nor any change of boundary vector.

For completeness define
\[
 B_{-,j}=b_{-,j}\cdots b_{-,1},\qquad
 H_j=B_{-,j-1}^{-1}G_{0,j}B_{-,j-1}.
 \tag{25}
\]
The two-strand identities (23) give
\[
                    H'_2=H_1,\qquad
                    H'_1=H_1^{-1}H_2H_1 .
 \tag{26}
\]
Indeed
\((b'_{-,2}b'_{-,1})^{-1}b'_{+,2}b'_{-,1}
 =b_{-,1}^{-1}b_{+,1}=H_1\);
the conserved total product gives the other equality.
For adjacent strands the common earlier prefix conjugates
these equations; the conserved local product keeps every later
prefix unchanged. Thus (25) obeys the Hurwitz relations for
the entire original word. Full closure yields the usual braid
presentation of the knot group.

In the meridian convention of [M] the actual group generators
are \(\mu_j=-H_j\). This central sign preserves (26).
The retained cut is
\[
                  \mu_1=\operatorname{diag}(-x_0,-x_0^{-1}).
 \tag{27}
\]
Its highest eigenline is the first coordinate line, with
eigenvalue \(M=-x_0\). The averaged-cut \(M^{-1}\) eigenflag
of [M, (5.4)--(6.1)] is not used.

## 5. Irreducibility, descent, and the original marks

At \(z\ne0\), the two eigenvalues in (27) are distinct.
Any common invariant line of the representation must therefore
be one of the two coordinate lines.

If all \(H_j\) preserve the second coordinate line, then all
their upper-right entries vanish. Each lower triangular prefix
in (25) preserves that line, so \(e_j=0\) for every \(j\).
By (4), all input momenta vanish. This contradicts the nonzero
vector \(P=Lp\) in (21).
If all \(H_j\) preserve the first coordinate line, argue by
induction in \(j\). The first has \(f_1=0\). If all preceding
\(f_i\) vanish, their lower prefixes are diagonal; the lower-left
entry of \(H_j\) then forces \(f_j=0\). Thus every input creation
field vanishes, contradicting the nonzero vector \(Z\) in (21),
which equals the input vector after closure. The representation
is irreducible.

On \(z=s^2\), choose the holomorphic
\(\sqrt{x_g(z)}=s\sqrt{x_g(z)/z}\). Equations (18) and all local
maps give a holomorphic representation germ in \(s\).
Balancedness sends \((Z,P)\) to
\((\lambda Z,\lambda^{-1}P)\) when
\((A,B_s)\) is sent to \((\lambda A,\lambda^{-1}B_s)\).
In (4) this fixes \(K\) and sends
\((e,f)\) to \((\lambda^{-1}e,\lambda f)\).
It is simultaneous diagonal conjugation in (22)--(25).
In particular \(s\mapsto-s\) conjugates all meridians by
\(\operatorname{diag}(i,-i)\). Traces of every group word are
even holomorphic functions of \(s\), and hence holomorphic in
\(z\). At \(z=0\) all fields vanish and the representation is
abelian. The same gauge calculation shows that choosing any
other nonzero \(A,B_s\) with product \(x_g\) changes only the
representative, not its character.

Finally retain the independent stage marks of [A].
A one-coordinate mark has generating phase
\(Z^T\operatorname{diag}(1,\ldots,e^{t_i},\ldots,1)p\).
Its derivative at \(t_i=0\) is exactly the stage occupation
\(Z_ip_i\). Differentiating a finite stationary composition
eliminates the derivatives of its intermediate critical fields.
The same envelope identity applies to the hard and soft
eliminations. Therefore
\[
       \Theta_{g,i}(z)
       =\left.\partial_{t_i}\Psi(z,x_g(z),\mathbf t)
                                                    \right|_{\mathbf t=0}
       =\text{the corresponding stage occupation}.
 \tag{28}
\]
Every original matching-lattice clock follows by its prescribed
linear combination of these occupations. No coordinate is
discarded because its value happens to be zero.
Consequently the formal leading clock ratio
\(\exp(m\cdot\Theta_g(z))\) is the analytic character obtained by
evaluating these additive clock observables at the constructed
representation point. This statement concerns the principal
stationary sector and does not assert its identification with a
continued marked Borel minor.

## 6. Scope and complete proof directs

The assertion uses the actual analytic phase and its nonzero
quadratic soft coefficient. It does not manufacture an Alexander
seed when \(\Delta=1\), prove that this representation component
is hyperbolic, identify peripheral action derivatives, or establish
a quantum source-cycle coefficient. In particular it does not
settle arbitrary fixed short partial fillings.

| Label | Complete proof source | SHA256 |
|---|---|---|
| A | notes/research_actual_analytic_principal_phase.md | 9ae7b5df2dbd955ee6ac4580590d9f21d1b1750bcdd6c5085e7322251ab70bcb |
| M | notes/marked_braid_holonomy.md | eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f |

A supplies the literal signed kernel potentials, analytic principal
composition, original highest-cut covariance, hard implicit equations,
and calibrated critical point. M supplies the Gauss/meridian
conventions and braid-group presentation. The local identities used
from M are rechecked above; its averaged-cut globalization, numerical
audits, geometric-chart assertion, and longitude calculation are not
proof premises here. The field extension, original cut closure,
irreducibility, and mark evaluation are proved in this note.

Only written mathematics, source reads, and hash checks were used.
Frozen notes and public manuscripts are unchanged.
