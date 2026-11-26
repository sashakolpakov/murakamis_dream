# The original routed period is a sum of actual cut currents

Private written proof, 18 November 2026.

At completeness the original pivotal source has the exact identity
\[
 \boxed{\quad
 \Phi=\frac{\varkappa_\beta}{1-Q^{-1}}
                 \sum_{r=1}^{N-1}J_r .
 \quad}                                                     \tag{1}
\]
Here the \(J_r\) are specified entries of the original cut current
transported by a literal block braid. No current is replaced by its
principal symbol. The factor in (1) has modulus
\((2\sin(\pi/N))^{-1}\), hence is of order \(N\).
The original scalar line \(\varkappa_\beta\) remains separate and
unchanged.

This follows from an exact Cartan comparison for the routed clock,
a forced first-difference equation for its source residues, and the
original pivotal geometric sum. A constant reduced matrix contributes
zero to that sum. Thus near-flatness alone would not supply a lower
bound for this period.

The proof retains all marked defects and, before root specialization,
the tail-pivot current and the nonzero constant-anchor row. It does
not identify the currents with a geometric relative interval or
prove their noncancellation.

## 1. Literal matrices, normal germ, and the corrected clock

Fix \(N\ge2\), \(q_N=e^{\pi i/N}\), \(Q=q^2\), \(x=-M/q\).
Use the actual balanced finite heads and zero arrows of B/W:
\[
 K w_a=xQ^{-a}w_a,\qquad
 \mathcal E w_a=(MQ^{-a}-M^{-1})w_{a-1}\quad(a>0),
 \qquad \mathcal E w_0=0,
\]
\[
 Fw_a=(1-Q^{a+1})w_{a+1}\quad(a<N-1),\qquad Fw_{N-1}=0.
                                                               \tag{2}
\]
Work on a sufficiently small fixed-\(N\) germ at \(q=q_N,M=1\).
All \(F_n(Q)=\prod_{k=1}^n(1-Q^k)\), \(n<N\), and
\(\alpha_r=MQ^{-r}-M^{-1}\), \(1\le r<N\), are units there.
Away from the root and ordinary-color path these compressed arrays
are not declared Hopf representations.

Let \(j\) be S's routed head. Its preceding ordered block has
\[
 K_p=\prod_{i<j}K_i,\qquad
 F_p=F_1+K_1^{-1}F_2+\cdots+
                       K_1^{-1}\cdots K_{j-2}^{-1}F_{j-1}.
                                                               \tag{3}
\]
Write \(J_j,J_p\) for its donor occupation and prefix total.
Put \(x_p=x^{j-1}\), so \(K_p=x_pQ^{-J_p}\), and define
\[
 A_0=\mathcal E_jF_p,\quad
 Y=K_j^{-1}\mathcal E_jK_pF_p,\quad
 D_p=x_p^{-J_j}x^{-J_p}Q^{J_jJ_p},\quad H=q^{J_j}.
                                                               \tag{4}
\]
All these are literal finite matrices. Both \(A_0^N\) and \(Y^N\)
vanish because the donor occupation strictly decreases.

S's routed insertion \(T\) has degree-zero part
\[
 T^{(0)}=\frac{-K_j+\mathcal E_jK_pF_p-dI}{c},
 \qquad c\ne0,                                                \tag{5}
\]
and a degree-\(+1\) part, with respect to total integer occupation.
Its exact diagonalizer is
\[
 \mathcal U=\sum_{n=0}^{N-1}\frac{Q^nY^n}{F_n(Q)},\qquad
 -K_j+\mathcal E_jK_pF_p=\mathcal U^{-1}(-K_j)\mathcal U .
                                                               \tag{6}
\]
The reference constants \(c,d\) are those of S, not state indices.

Use the explicitly corrected insertion
\[
                       T^\sharp=H^{-1}TH .                    \tag{7}
\]
It is an insertion in the same finite source. It is not silently
identified with \(T\). Its regular interior principal coordinate
is the same: conjugation multiplies every fixed shift by an
integer power of \(q\) with fixed exponent, which tends to one.
Neither mark is asserted to descend through every principal
momentum quotient. The balanced or inverse-free eigenflag marks
have additional coupons and are addressed in Section 8.

## 2. Exact Cartan dressing and an actual block-braid route

The two weight changes in (4), evaluated on an input
\((a,b)=(J_j,J_p)\), give exactly
\[
 D_pA_0D_p^{-1}=QY,\qquad HA_0H^{-1}=q^{-1}A_0 .                \tag{8}
\]
For the first identity the Cartan ratio is
\((x_p/x)Q^{a-b-1}\), whereas \(Y/A_0\) on the output is
\((x_p/x)Q^{a-b-2}\). This verifies the order as well as the
factor \(Q\).

The literal Euler polynomial and inverse of B are
\[
 \Theta(A_0)=\sum_{n<N}\frac{(-1)^nq^{n^2}A_0^n}{F_n(Q)},
 \qquad
 \Theta(A_0)^{-1}=\sum_{n<N}\frac{q^nA_0^n}{F_n(Q)}.
                                                               \tag{9}
\]
Their inverse identity is finite modulo \(A_0^N=0\).
Consequently (8) proves
\[
 \mathcal U=D_pH\Theta(A_0)^{-1}H^{-1}D_p^{-1}.
                                                               \tag{10}
\]
Set \(R_0=D_p\Theta(A_0)\). Since \(D_p,H\) and the donor
projectors \(P_a^{(j)}\) commute, (10) yields
\[
 \mathcal U^{-1}P_a^{(j)}\mathcal U
       =H R_0P_a^{(j)}R_0^{-1}H^{-1}.                          \tag{11}
\]
Thus the degree-zero spectral projectors of \(T^\sharp\) are
exactly \(R_0P_a^{(j)}R_0^{-1}\). The half-head factor in (11)
would remain for the original \(T\).

This \(R_0\) has a literal braid interpretation, including its
ordering. First relabel the tensor factors as
\[
       V_j\otimes(V_1\otimes\cdots\otimes V_{j-1})
                        \otimes V_{j+1}\otimes\cdots\otimes V_b.
                                                               \tag{12}
\]
The uncheck crossing of the first head with the ordered block is
\(\kappa_{\rm block}D_p\Theta(\mathcal E_jF_p)\).
Its checked block permutation restores the original order.
Denote that checked operator by
\(\mathscr B:\mathcal H_{\rm new}\longrightarrow\mathcal H_{\rm old}\).
It is the actual adjacent crossing word moving the donor to the
right past heads \(1,\ldots,j-1\).

Here is why this block formula specializes as a whole actual matrix.
R proves
\((1\otimes\Delta)R=R_{13}R_{12}\) by ordered finite Gaussian
binomial coefficients and the Cartan commutations; iteration gives
the displayed block order. The coefficient identity uses only the
weight relations, and the total donor transfer on an input
\(a_j<N\) is less than \(N\). Thus every denominator remaining
after evaluation is one of the units \(F_n\), \(n<N\).
On each recipient the transfer only raises its occupation. A path
which exits a physical recipient head cannot return during this
block word. Therefore compressing the coefficient identity is the
same as using the original truncated arrows at every crossing.
This also proves the identity for the auxiliary finite arrays on
the normal germ, without a generic Hopf premise.

The common scalar \(\kappa_{\rm block}\) is the product of the
original crossing Cartan lines. It is included in \(\mathscr B\);
it cancels, rather than being reset, in its conjugations. With the
tensor relabeling (12) understood, (11) becomes
\[
        \Pi_a^\sharp=\mathscr B P_a^{(1)}\mathscr B^{-1}.
                                                               \tag{13}
\]
This is a genuine second-cut route. It does not replace the first
cut by a scalar.

## 3. The original residue weights after routing

Let \(\mathcal W\) be the actual whole degree-zero word, with any
degree-zero coupons and diagonal clocks retained. Let
\[
 P=T_0^{(1)}\otimes g^{\otimes(b-1)},\qquad g=K^{1-N},\qquad
 \Phi=\varkappa_\beta\operatorname{Tr}(P\mathcal W).              \tag{14}
\]
No assumption is made that a marked \(\mathcal W\) intertwines.
For a different explicitly specified diagonal cut the same
calculation uses its conjugated probe; (14) fixes the original
highest presentation here.

Because \(gT_0=x^{1-N}T_0\),
\[
                    P=x^{N-1}g_{\rm tot}T_0^{(1)}.             \tag{15}
\]
Define, on the new ordering (12),
\[
 O=\mathscr B^{-1}\mathcal W\mathscr B,\qquad
 \mathcal Q=\mathscr B^{-1}T_0^{(1)}\mathscr B .
                                                               \tag{16}
\]
Both preserve total integer occupation. The block braid preserves
that occupation as well, so it transports \(g_{\rm tot}\) to the
same product in the new ordering.

On the remaining heads put
\[
 K_R=\prod_{\rm rest}K_i,\qquad g_R=K_R^{1-N},\qquad
 C=\operatorname{Tr}_R(g_R O\mathcal Q).                        \tag{17}
\]
The matrix \(C\) on the distinguished head is diagonal. Indeed, a
term in its partial trace has identical incoming and outgoing
indices on every other head; degree zero then forces equality on
the distinguished head too. Write its diagonal entries \(C_a\).

S's degree filtration removes the positive-degree part of the
resolvent inside this diagonal source trace. Its simple-pole
weights for \(T^\sharp\), with
\(\lambda_a=(-xQ^{-a}-d)/c\), are therefore
\[
 \begin{split}
 w_a&=\varkappa_\beta
          \operatorname{Tr}(P\Pi_a^\sharp\mathcal W)\\
    &=\varkappa_\beta x^{N-1}g_a C_a,\qquad
 g_a=x^{1-N}Q^{(N-1)a}.
 \end{split}                                                  \tag{18}
\]
For the second equality use (13)--(16), then cyclicity and the
commutation of \(O\) with total occupation. In particular
\[
              \Phi=\sum_aw_a
               =\varkappa_\beta\sum_{a=0}^{N-1}\omega^a C_a,
                    \qquad \omega=Q^{N-1}.                    \tag{19}
\]
The factors \(x^{N-1}\) and \(g_0\) cancel exactly in (19).
All pivotal phases remain.

## 4. A forced first-difference equation with its whole normal current

Use either \(Z=\mathcal E\) or \(Z=KF\). Its ordered coproduct
on (12) is
\[
                     Z_{\rm tot}=Z_1K_R+Z_R .                 \tag{20}
\]
For \(KF\) this follows directly from
\(\Delta F=F_1+K_1^{-1}F_R\) and
\(\Delta K=K_1K_R\). Put \(Y_R=K_R^{-N}\).
Ordinary partial cyclicity, with no specialization, proves
\[
 \boxed{\begin{split}
 [Z_1,C]=\mathcal J_Z:={}&
 \operatorname{Tr}_R\!
    \left(Y_R([Z_{\rm tot},O]\mathcal Q
                         +O[Z_{\rm tot},\mathcal Q])\right)\\
 &-\operatorname{Tr}_R([Y_R,Z_R]O\mathcal Q).
 \end{split}}                                                 \tag{21}
\]
To verify every term, put \(V=O\mathcal Q\). The
\(Z_1K_R\) part of
\(\operatorname{Tr}_R(Y_R[Z_{\rm tot},V])\) is \([Z_1,C]\),
since \(Y_RK_R=g_R\). Its other part is
\(\operatorname{Tr}_R([Y_R,Z_R]V)\). This proves (21) and its
minus sign. No cyclicity on the distinguished head was used.

At the root, \(Y_R\) commutes with \(Z_R\), since its weight is an
integer power of \(Q^N=1\). For an unmarked actual braid word,
the block intertwining also gives \([Z_{\rm tot},O]=0\), and
\[
 [Z_{\rm tot},\mathcal Q]
     =\mathscr B^{-1}
          [Z_{\rm tot}^{\rm old},T_0^{(1)}]\mathscr B .         \tag{22}
\]
The forcing is then precisely the transported original cut-arrow
current. Arbitrary marks keep their first term in (21).
No scalarity of a second-cut environment is assumed.

For \(Z=\mathcal E\), define
\[
               J_r=(\mathcal J_{\mathcal E})_{r-1,r},
                       \qquad 1\le r<N.
\]
The entries of (21) are exactly
\[
                  \alpha_r(C_r-C_{r-1})=J_r,\qquad
                  \alpha_r=MQ^{-r}-M^{-1}.                    \tag{23}
\]
Hence on the specified unit germ
\[
                       C_a=C_0+\sum_{r=1}^aJ_r/\alpha_r .
                                                               \tag{24}
\]
The \(KF\) row is a second, retained finite equation. Neither row
is made homogeneous by the original intertwining property.

## 5. Pivotal telescoping and the actual \(N\)-scale

Before either specialization, substitution of (24) in (19) gives
the finite identity
\[
 \Phi=\varkappa_\beta\left[
       S_N(\omega)C_0+
       \sum_{r=1}^{N-1}S_{r,N}(\omega)\frac{J_r}{\alpha_r}
                          \right],
 \quad
 S_N(\omega)=\sum_{a=0}^{N-1}\omega^a,\quad
 S_{r,N}(\omega)=\sum_{a=r}^{N-1}\omega^a .                     \tag{25}
\]
The finite sums, including their values at \(\omega=1\), are used.

At \(q=q_N\), \(\omega=Q^{-1}\), and
\[
 S_N(Q^{-1})=0,\qquad
 S_{r,N}(Q^{-1})=\frac{Q^{-r}-1}{1-Q^{-1}} .
                                                               \tag{26}
\]
For the root meridian germ this yields
\[
 \Phi=\frac{\varkappa_\beta}{1-Q^{-1}}
       \sum_{r=1}^{N-1}
          \frac{Q^{-r}-1}{MQ^{-r}-M^{-1}}\,J_r .                \tag{27}
\]
At \(M=1\) every displayed ratio is one, proving (1).
The factor and its phase are explicit:
\[
 \frac1{1-Q^{-1}}
       =\frac{e^{\pi i/N}}{2i\sin(\pi/N)},\qquad
 \left|\frac1{1-Q^{-1}}\right|
                 \sim\frac{N}{2\pi}.                          \tag{28}
\]
This is an actual source-current adapter. It is not evidence by
itself for an \(N\)-fold geometric framing path.

For normal derivatives of the specified auxiliary source germ use
(21) and (25) first, including
\([Y_R,Z_R]\), every marked intertwining defect, \(C_0\),
and \(S_N(\omega)\). One may restrict \(M=-q^N\), with \(N\)
fixed, and differentiate with its full chain rule, but these
formulas still retain the explicitly defined ADO pivot
\(g=K^{1-N}\). The path alone does not identify the resulting
closed jets with ordinary colored-Jones jets. Such a comparison
requires the whole prescribed ordinary pivot/twist adapter as
additional source data before differentiation; no equality of
those closed normalizations is asserted here.
The constant anchor row is not identically zero off the root.
Differentiating (1) or (26) as an off-root identity would omit it
and the tail current. Fixed-root meridian normals use the whole (27).

## 6. A direct closing current on any original pivotal head

Rivin's finite-head calculation gives a second form of the same
scale, without a routed mark or an intertwining hypothesis.
Choose any tail head carrying its original \(g=K^{1-N}\) in \(P\).
Let \(Lw_a=w_{a-1}\) for \(a>0\), \(Lw_0=0\), and put
\[
 Q_{\rm f}=-q^{-1}L,\qquad
 \delta=1-Q^N,\quad \gamma=Q^{1-N},\quad \rho=q-q^{-1}.
                                                               \tag{28a}
\]
The two diagonal products of the literal \(F\) and \(L\) give
\[
 LF-QFL=(1-Q)I-\delta P_{N-1},
 \qquad
 Q_{\rm f}F-QFQ_{\rm f}
                   =\rho I+q^{-1}\delta P_{N-1}.               \tag{28b}
\]
For rows below \(N-1\) the first identity is
\((1-Q^{a+1})-Q(1-Q^a)=1-Q\). On the top row its left
side is \(-Q(1-Q^{N-1})\), giving exactly the displayed
correction. The vacuum row is included.

Also \(gQ_{\rm f}=\gamma Q_{\rm f}g\).
All other tensor factors of \(P\) commute with this coupon.
For any whole finite word \(\mathcal W\), now without a
degree restriction, multiply (28b) by \(\mathcal W\) in the
original functional. Cyclicity gives
\[
 \Phi(Q_{\rm f}F\mathcal W)
                   =\gamma\Phi(F\mathcal W Q_{\rm f}).
\]
Since \(\gamma-Q=\gamma\delta\), the exact result is
\[
 \boxed{\begin{split}
 \rho\Phi(\mathcal W)
   ={}&\gamma\Phi(F[\mathcal W,Q_{\rm f}])\\
      &+\delta\{\gamma\Phi(FQ_{\rm f}\mathcal W)
                     -q^{-1}\Phi(P_{N-1}\mathcal W)\}.
 \end{split}}                                                 \tag{28c}
\]
Here \(\Phi(V)=\varkappa_\beta\operatorname{Tr}(PV)\);
the original cut and every other pivot are unchanged.
The commutator expands in the original word order through
all crossings, marks, and coupons.

At the root this specializes to
\[
                  \Phi(\mathcal W)
                    =\frac Q\rho\,\Phi(F[\mathcal W,Q_{\rm f}]).
                                                               \tag{28d}
\]
At completeness, for the same degree-zero source as above,
\((1-Q^{-1})^{-1}=q/\rho\), so comparison with (1) gives
\[
       \varkappa_\beta\sum_{r=1}^{N-1}J_r
                         =q\,\Phi(F[\mathcal W,Q_{\rm f}]).
                                                               \tag{28e}
\]
These are two presentations of one current scale, not two
multiplicative factors of \(N\).
For derivatives of this same ADO-pivot source germ retain (28c),
including \(\delta,\gamma,P\) and the entire scalar line.
Any path restriction uses its full chain rule and the normalization
qualification of Section 5. An ordinary closed-color comparison
must first retain its whole pivot/twist adapter.
No top-row normal is discarded.
The coupon has norm one at the physical root, but this does
not bound its commutator's contraction with an arbitrary word.

## 7. Quantitative inversion and a correctly phased criterion

At completeness
\[
 |\alpha_r|=2\sin(\pi r/N)
       \ge4\min(r,N-r)/N .
 \]
The two harmonic sums give, for every \(N\ge2\),
\[
 \max_a|C_a-C_0|
      \le N(1+\log N)\max_{1\le r<N}|J_r|.                     \tag{29}
\]
Thus the forced row has a polynomially conditioned reconstruction
from an anchor and its actual current entries. This estimate does
not say those currents are small.

In particular, even if all \(C_a\) are close to a nonzero common
anchor, its contribution to the original period is exactly zero
by (26). An unweighted lower bound for \(\sum C_a\) is not a
lower bound for (19).

A sufficient condition which does apply to the original source
can instead be stated on the current entries. If a nonzero
complex number \(J_*\) satisfies
\[
             \sum_{r=1}^{N-1}|J_r-J_*|
                        \le\tfrac12(N-1)|J_*|,
                                                               \tag{30}
\]
then (1) gives
\[
 |\Phi|\ge
   \frac{|\varkappa_\beta|(N-1)|J_*|}
                         {2|1-Q^{-1}|}.                      \tag{31}
\]
This is a conditional phase-coherence criterion for specified
finite source currents, not an asserted property of a short
tangle or of its geometric component.

## 8. Scope of the reduction

The exact block route fixes which original probe accompanies the
clock projectors. The first-difference row and the pivotal sum then
express the original period through that probe's actual cut and
marked currents. Their sum remains unknown.

For S's original mixed-degree \(T\), the half-head dressing \(H\)
in (11) must also be retained in the transformed word and probe;
its commutators enter (21). The balanced and unilateral flag marks
contain an additional eigenflag coupon multiplying
\(\widehat\mu_{j,21}\). They do not share the clock projector
identity (13) merely because their principal restriction is
\(r/s\). Their extra coupon changes the source equations.
No clock spectrum, universal weights, or scalar q-Hahn reduction
is transferred to them here.

Nothing identifies the finite current sum in (1) with a geometric
endpoint divisor or controls same-action endpoint layers. The
construction supplies neither a physical-cycle coefficient nor
an exponential lower bound without the additional input in (30)
or another proved noncancellation mechanism.

## Complete proof-source pins

* S: notes/research_actual_routed_spectral_current.md,
  SHA256 5377af960664dd6b29af223980a9d857ffb8553420d9dafe182412eb402783c8.
* W: notes/research_actual_weighted_ward_centralizer_lift.md,
  SHA256 e689364ab8e756ef51f8da43a7ea86d84086afd6bf57ffbe0af1a4f508c2648a.
* B: notes/balanced_verma_coherent_braiding.md,
  SHA256 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.
* R: notes/regular_holonomy_braiding.md,
  SHA256 5be349365f59c89d4e20ce411a93baa850562056b62b13ad4d465b1b1607f9ef.

All four complete texts were read nontruncated in the active
author/formal-review sequence, retained unchanged where applicable,
and their used implications checked. Only written mathematics and
text/hash operations were used. No frozen or public file was edited.
