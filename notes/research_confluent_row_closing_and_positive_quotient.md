# Confluent physical rows, the original closing, and the turn-invariant positive quotient

Private written proof, 17 November 2026.

The full physical value and normal rows give an exact block formula
for the original Frobenius closing. They also identify the largest
positive quotient on which every original \(V_n\) is an isometry.
The prescribed closing has dual norm one on this quotient, but one
literal multiplication crossing does not descend to it. In fact
the same obstruction applies to every positive semidefinite form
invariant under \(V_1\) which controls that closing.

These are statements about the original finite source and its full
normal channels. They give neither a lower bound for a prescribed
filled scalar nor a source-specific geometric asymptotic.

## 1. Full original rows and conventions

Put
\[
 N\ge2,\quad D=N-1,\quad J=\lfloor D/2\rfloor,\quad
 \theta=\pi/N,\quad q=e^{i\theta},\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 c_j=2\cos((2j+1)\theta),\quad
 P_N(Z)=2T_N(Z/2)+2,\quad
 \mathcal A_N=\mathbb C[Z]/(P_N).
 \tag{1}
\]
Here \(T_N\) in \(P_N\) is the Chebyshev polynomial.
The distinct double-node indices form
\(\mathcal D_N=\{0,\ldots,\lfloor N/2\rfloor-1\}\).
At odd \(N\), the remaining index \(j=J\), denoted by \(*\)
when convenient, is the simple node \(c_*=-2\).

With \(s_r=2\sin(r\theta)\), \(S_r=\prod_{a=1}^r s_a\), and
\(S_0=1\), retain
\[
 e_r(Z)=S_r^{-2}\prod_{a<r}(c_a-Z),\qquad
 K_N(w,Z)=\sum_{r=0}^{D}e_r(w)e_r(Z),
\]
\[
 \phi_N(f)=\eta N^2[Z^D]\operatorname{rem}_{P_N}f,\qquad
 Te_r=e_{D-r},\qquad
 V_n=\kappa^nTR^{-n}T .
 \tag{2}
\]
Here \(R\) and its powers mean the original multiplication
crossings, with their common Cartan scalar retained. The physical
rows are
\[
 F_j=K_N(c_j,\cdot),\qquad
 G_j=\partial_wK_N(c_j,\cdot)\quad(j\in\mathcal D_N).
 \tag{3}
\]
The signed linearization source proves that these rows form a
basis: \(\deg F_j=j\), \(\deg G_j=D-j\). There is no \(G_*\)
at the odd simple node.

The original Newton identities give
\[
 \phi_N(e_r e_s)=\mathbf1_{r+s=D},\qquad
 \phi_N(Tf\,Tg)=\phi_N(fg),\qquad
 \phi_N(Tf)=f(c_0).
 \tag{4}
\]
The middle identity follows directly by reversing both indices
in the first identity. Thus \(T\) preserves this bilinear
Frobenius form. It is not an algebra homomorphism.

## 2. Exact confluent Gram and coordinate recovery

For a double node define
\[
 a_j=4-c_j^2,\qquad
 \beta_j=\frac{\eta}{a_j},\qquad
 \gamma_j=\frac{\eta c_j}{a_j^2}.
 \tag{5}
\]
Both \(a_j\) and \(\beta_j\) are nonzero.

**Theorem 1.** In the basis (3), distinct physical nodes are
orthogonal for the bilinear form \((f,g)\mapsto\phi_N(fg)\).
The double-node block and odd simple block are respectively
\[
 \boxed{\quad
 \begin{pmatrix}
 \phi_N(F_j^2)&\phi_N(F_jG_j)\\
 \phi_N(F_jG_j)&\phi_N(G_j^2)
 \end{pmatrix}
 =
 \begin{pmatrix}0&\beta_j\\ \beta_j&\gamma_j\end{pmatrix},
 \qquad \phi_N(F_*^2)=1 .
 \quad}
 \tag{6}
\]
For
\[
 f=\sum_{j\in\mathcal D_N}(A_jF_j+B_jG_j)
          +\mathbf1_{N\ {\rm odd}}A_*F_*,
 \tag{7}
\]
its coefficients are exactly
\[
 \boxed{\quad
 B_j=\beta_j^{-1}(Tf)(c_j),\qquad
 A_j=\beta_j^{-1}(Tf)'(c_j)
                  -\gamma_j\beta_j^{-2}(Tf)(c_j),\qquad
 A_*=(Tf)(-2).
 \quad}
 \tag{8}
\]
In particular the actual prescribed closing is
\[
                  \boxed{\ \phi_N(f)=\beta_0 B_0.\ }
 \tag{9}
\]

**Proof.** The ordinary reproducer and its first normal give
\[
 TF_j=\delta_j=\frac{P_N(Z)}{\eta N^2(Z-c_j)},\qquad
 TG_j=\epsilon_j=\frac{P_N(Z)}{\eta N^2(Z-c_j)^2},
 \tag{10}
\]
\[
 \phi_N(\delta_j f)=f(c_j),\qquad
 \phi_N(\epsilon_j f)=f'(c_j).
 \tag{11}
\]
The second identity is only used at double nodes. All fractions
in (10) are polynomials; (11) includes canonical multiplication
and the full repeated-root relation.

The Chebyshev differential equation and its derivative are
\[
 (4-Z^2)P_N''-ZP_N'+N^2(P_N-2)=0,
\]
\[
 (4-Z^2)P_N'''-3ZP_N''+(N^2-1)P_N'=0 .
 \tag{12}
\]
At a double root these imply
\[
 \frac{P_N''(c_j)}{2\eta N^2}=\beta_j,\qquad
 \frac{P_N'''(c_j)}{6\eta N^2}=\gamma_j .
 \tag{13}
\]
Thus \(\delta_j(c_j)=0\), \(\delta_j'(c_j)=\beta_j\),
\(\epsilon_j(c_j)=\beta_j\), and
\(\epsilon_j'(c_j)=\gamma_j\).
At every other double node both polynomials have the required
zero value and first normal, except that only the value is
required at the odd simple node. At that simple node
\(\delta_*(-2)=P_N'(-2)/N^2=1\).
Equations (4), (10), and (11) now give (6).
The physical jets of \(Tf\) in (10) give (8).

Finally \(\phi_N(f)=(Tf)(c_0)\), by applying (4) to \(Tf\).
The value at \(c_0\) in (8) is \(\beta_0B_0\), proving (9).
The simple row contributes nothing to (9). \(\square\)

For the coefficient reflection
\(f^\sharp(Z)=\overline{f(\bar Z)}\), the Hermitian form
\(\phi_N(f^\sharp g)\) has the same real blocks (6).
Every double block has determinant \(-\beta_j^2<0\).
Its total signature is
\((\lceil N/2\rceil,\lfloor N/2\rfloor)\).
In particular the span of the value rows is totally isotropic
at even levels. At odd levels its only nonzero pairing is the
simple-row square. These conclusions also follow from the
degrees in (3), but (6) retains the missing normal pairings.

## 3. Actual Jordan phases and all invariant positive forms

Write
\[
 \nu_j=(-1)^j q^{j(j+1)},\qquad
 \lambda_{n,j}=\nu_j^{-n},\qquad
 \alpha_j=\frac{R'(c_j)}{R(c_j)}
          =\frac{i(D-2j)}{4\sin((2j+1)\theta)}
                 \quad(j\in\mathcal D_N).
 \tag{14}
\]
The original crossing values are \(R(c_j)=\kappa\nu_j\).
The number \(\alpha_j\) is purely imaginary and nonzero at
every double node, at every \(N\ge2\).
The retained Jordan action from the signed-turn source is
\[
 V_nF_j=\lambda_{n,j}F_j,\qquad
 V_nG_j=\lambda_{n,j}(G_j-n\alpha_jF_j).
 \tag{15}
\]
The odd simple row has only its first formula.
Thus (7) transforms by
\[
       (A_j,B_j)\longmapsto
          \lambda_{n,j}(A_j-n\alpha_jB_j,B_j).
 \tag{16}
\]
The normal coefficient is not discarded. The Hermitian
indefinite form (6) is preserved by (16), since
\(\alpha_j+\overline{\alpha_j}=0\) and \(|\lambda_{n,j}|=1\).

Define the surjective value map and its seminorm by
\[
 \mathcal U_N f=((Tf)(c_j))_{0\le j\le J},\qquad
 \|f\|_{\mathcal Q_N}^2
       =\sum_{j=0}^{J}|(Tf)(c_j)|^2 .
 \tag{17}
\]
Surjectivity follows from ordinary value interpolation,
followed by \(T\); prescribing no normals is required for it.

**Theorem 2.** The form (17) has exactly the kernel
\[
        \mathcal L_N=\operatorname{span}
                         \{F_j:j\in\mathcal D_N\}.
 \tag{18}
\]
It gives a positive definite norm on
\(\mathcal A_N/\mathcal L_N\), and every \(V_n\) induces an
isometry there. The original closing descends and satisfies
\[
             |\phi_N(f)|\le\|f\|_{\mathcal Q_N}
 \tag{19}
\]
with exact dual norm one.

Moreover, every positive semidefinite Hermitian form
\(\mathfrak h\) on \(\mathcal A_N\) satisfying
\(\mathfrak h(V_1f,V_1g)=\mathfrak h(f,g)\) kills
\(\mathcal L_N\). Precisely all such forms are
\[
 \mathfrak h(f,g)=(\mathcal U_N f)^* B(\mathcal U_N g),
 \quad B\ge0,\quad
 B_{jk}=0\ \hbox{if }\lambda_{1,j}\ne\lambda_{1,k}.
 \tag{20}
\]
Possible repeated crossing phases are retained in the blocks
of \(B\), including at composite levels.

**Proof.** Equation (8) proves (18). Also, directly from (2),
\[
 \mathcal U_N(V_nf)_j
   =\kappa^nR(c_j)^{-n}(Tf)(c_j)
   =\lambda_{n,j}\mathcal U_N(f)_j .
 \tag{21}
\]
This proves isometry. Equation (9) identifies the closing
with the zeroth coordinate of (17), proving (19).
Equality is achieved by \(f=\beta_0^{-1}G_0\), whose
\(\mathcal U_N\) vector is the zeroth standard vector.

For any invariant \(\mathfrak h\), iterate (15) with \(n=m\)
and \(m\) an arbitrary positive integer:
\[
 \mathfrak h(G_j-m\alpha_jF_j,G_j-m\alpha_jF_j)
                       =\mathfrak h(G_j,G_j).
 \tag{22}
\]
The coefficient of \(m^2\) is
\(|\alpha_j|^2\mathfrak h(F_j,F_j)\), so it is zero.
Positivity and Cauchy--Schwarz then give
\(\mathfrak h(F_j,g)=0\) for every \(g\).
Thus the form factors through (17), giving a unique matrix
\(B\ge0\). Invariance under the unit diagonal matrix in
(21) is precisely the block condition in (20).
Conversely that condition proves invariance, and also
invariance under every \(V_n=V_1^n\). \(\square\)

The quotient in (18) is a quotient of vector spaces with the
specified \(V_n\) action. It is not an algebra quotient:
it kills \(F_0=1\). It retains the normal coefficients \(B_j\)
through \((Tf)(c_j)=\beta_j B_j\), but forgets their value-row
partners. No assertion about serial products follows from its
positive norm.

For \(N\ge3\), (19) has no converse lower bound on the full
quotient. A coordinate of \(\mathcal U_N f\) other than zero
can be nonzero while \(\phi_N(f)=0\); take \(G_j\) with
\(j>0\) when available, or the odd simple row.
At \(N=2\) the quotient has dimension one, but the crossing
obstruction below still holds.

## 4. One original crossing leaves every such null quotient

The original finite crossing formulas are
\[
 R^\sigma=\kappa^\sigma
           \sum_{r=0}^{D}(-q)^{\sigma r}e_r,\qquad
                    \sigma\in\{1,-1\}.
 \tag{23}
\]
They imply the exact polynomial identities
\[
 TR^\sigma=R^{-\sigma},\qquad
             \phi_N(R^\sigma)=\kappa^\sigma(-q)^{\sigma D},
 \qquad |\phi_N(R^\sigma)|=1 .
 \tag{24}
\]
For the first identity reverse (23) and use
\(\kappa^2(-q)^D=1\). All original phases are retained.

**Theorem 3.** There is no positive semidefinite Hermitian
form \(\mathfrak h\) satisfying all three properties
\[
 \mathfrak h(V_1f,V_1f)=\mathfrak h(f,f),\qquad
 |\phi_N(f)|^2\le C_N\mathfrak h(f,f),
\]
\[
 \mathfrak h(R^\sigma f,R^\sigma f)
                      \le B_N\mathfrak h(f,f)
                  \quad\hbox{for every } f\in\mathcal A_N,
 \tag{25}
\]
where \(C_N,B_N\) are finite and \(\sigma\) is either one
of the two original crossing signs.
This holds separately at each level \(N\ge2\).

**Proof.** Theorem 2 forces \(\mathfrak h(1,1)=0\).
The last inequality in (25) then forces
\(\mathfrak h(R^\sigma,R^\sigma)=0\), and the second
forces \(\phi_N(R^\sigma)=0\). This contradicts (24).
\(\square\)

The contradiction uses the actual unit input and one literal
crossing; it does not require a coupon depending on an unknown
closed scalar. In particular no finite crossing bound exists
for (17), even if a level-dependent exponential constant is
allowed.

The full prescribed one-crossing observation in the confluent
basis is also explicit:
\[
 \phi_N(R^\sigma F_j)=R(c_j)^{-\sigma},\qquad
 \phi_N(R^\sigma G_j)
                    =-\sigma\alpha_j R(c_j)^{-\sigma}.
 \tag{26}
\]
Indeed \(\phi_N(F_jf)=(Tf)(c_j)\) and
\(\phi_N(G_jf)=(Tf)'(c_j)\), so (26) follows from (24).
The odd simple row uses only the first formula.
Combining (16) with (26), for every integer \(n\),
\[
 \phi_N(R^\sigma V_nf)
 =\kappa^{-\sigma}
     \sum_{j\in\mathcal D_N}
          \lambda_{n+\sigma,j}
                   \{A_j-(n+\sigma)\alpha_jB_j\}
   +\mathbf1_{N\ {\rm odd}}\kappa^{-\sigma}
          \lambda_{n+\sigma,*}A_* .
 \tag{27}
\]
Thus the crossing which exposes the null value rows also
retains the normal shears and their original quadratic phases.
Equation (27) is a coherent scalar sum, not a positive sum
or a lower estimate.

## 5. Scope and complete direct sources

The general indefinite-closing obstruction, the positive
Newton metric, and twist observation norms already have
separate proofs. The added statements here are the explicit
full \(F/G\) Gram and coordinate closing, the classification
(20) with its largest quotient (18), and the source-specific
incompatibility (25). Positive low-degree linearization alone
does not determine the \(G_0\) coefficient extracted in (9).
The positive Newton multiplication cone is also already known;
no new positivity theorem for that cone is claimed here.

Exact identities hold with arbitrary ordinary free spectator
coefficients. The positive forms and inequalities mean a
fixed complex specialization of those coefficients.
Subsequent products, turns, and traces remain the original
ones. Theorem 3 concerns exact \(V_1\) isometry on the whole
space; it does not exclude controlled distortion on a
restricted received source or a geometric norm with retained
exponential costs.

All three complete direct texts were read at the following
pins and their used implications checked:

* [Alternating physical-row linearization](research_physical_row_alternating_linearization.md),
  SHA256 326c55623da9155b6f5a0be4ab3e3b2584bdf7c568cd288d1e69569473c36342:
  full \(F/G\) basis, ordinary reproducers, and signed Jordan action.
* [Original positive Newton Gram](actual_newton_turn_positive_gram.md),
  SHA256 d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3:
  full Frobenius pairing, actual turn, and finite signed crossings.
* [Original twist observations](research_original_twist_observation_tomography.md),
  SHA256 6885ad1b82b8f67ddda497f969337a9230b17925fd88b4326b0152dfdc738a1c:
  exact crossing values and first normals, including all levels.

Only written proof, source-text reads, and metadata hashes were
used. No mathematical program, numerical experiment, test,
build, or compilation was run. Frozen sources and public
manuscripts are unchanged.
