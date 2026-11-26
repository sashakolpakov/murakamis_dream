# The original two-run source as a full-period monodromy jet

Research note, 3 November 2026.

The exact finite-channel recurrence for two crossing runs has a
distinguished reset at color zero. Retaining that reset identifies the
original closed source with a specified entry of the zeroth, first, or
second derivative of its full-period matrix. This works for every pair
of nonzero signed powers and both quantum-level parities. In particular,
the actual source for powers \((-4,-5)\) is a first derivative of a
seven-dimensional monodromy, with its scalar normalization fixed.

This is an identity for the original source. It is not a dominant-mode
or asymptotic theorem. The relevant derivative includes the accumulator
row, which a characteristic polynomial does not see.
Independent clock parameters also give an exact cyclic transport
equation for that marked row, including the reset.

## 1. Signed clocks and the original source

Fix \(N\ge2\), \(D=N-1\), \(q=\exp(\pi i/N)\), \(Q=q^2\), and
\(\kappa=\exp(\pi iD^2/(2N))\). Let \(M,J\) be the original crossing
and turn matrices in the complete Newton quotient. Thus all
double-root normals are retained. The
[resonant run formula](research_resonant_crossing_run_source.md)
and the [literal two-run transfer](research_two_run_source_transfer.md)
give, for fixed nonzero integers \(a,b\),
\[
 \mathcal Z_{a,b,N}
   =\phi_N(R^bT(R^a))
   =\mathbf e_D^TM^bJM^a\mathbf e_0
   =\sum_{j=0}^D(M^a)_{j0}(M^b)_{j0}.
 \tag{1}
\]
This is a bilinear pairing; conjugation is supplied only by actual
negative powers.

For a nonzero signed power \(p\), write
\[
 \sigma_p=\operatorname{sgn}p,\qquad
 k_p=\lceil |p|/2\rceil,\qquad q_p=q^{\sigma_p},\qquad
 Q_p=q_p^2,\qquad
 (v_p)_h=q_p^{k_p-h}\quad(1\le h\le k_p).
 \tag{2}
\]
Use the polynomial matrix from the two-run transfer:
\[
 \begin{split}
 (\mathcal B_k(r;q_0))_{ht}
 =r^{|h-t|+1}\left[
   \sum_{\nu=0}^{k-\max(h,t)}r^{2\nu}
  -\frac r{q_0}\sum_{\nu=0}^{k-\max(h,t)-1}r^{2\nu}
 \right].
 \end{split}                                                   \tag{3}
\]
An empty sum is zero. Introduce an auxiliary complex parameter \(z\)
near \(1\), and put \(\xi_{p,j}(z)=zQ_p^j\). Define
\[
 \mathcal T_p(j;z)=
 \begin{cases}
 (1-\xi_{p,j}^{-1})
       \mathcal B_{k_p}(q_p\xi_{p,j};q_p),& |p|\text{ even},\\[2mm]
 \mathcal B_{k_p}(q_p\xi_{p,j};q_p)
       \operatorname{diag}(-\xi_{p,j}^{-1},
                1-\xi_{p,j}^{-1},\ldots,1-\xi_{p,j}^{-1}),
                & |p|\text{ odd}.
 \end{cases}                                                    \tag{4}
\]
These matrices are holomorphic at \(z=1\). Negative powers use
\(q_p,Q_p\) as written, but the same holomorphic multiplier \(z\).
In particular, \(z\) is not conjugated. For opposite signs the two
physical clocks run in opposite directions. This auxiliary parameter
is not a free geometric boundary coordinate.
The matrices are periodic in the color \(j\) with period \(N\).
For opposite signs, however, a common change \(z\mapsto Qz\)
advances one physical clock and reverses the other. In general it
does not cyclically permute the factors of (12). The independent
parameters in Section 5 give the correct cyclic shift.

At \(z=1\), the original run states are
\[
 u_{p,0}=v_p,\qquad
 u_{p,j}=\mathcal T_p(j;1)u_{p,j-1}\quad(1\le j<N),\qquad
 (M^p)_{j0}=\kappa^p\mathbf e_{k_p}^Tu_{p,j}.
 \tag{5}
\]
No transfer at color zero is applied in (5).

## 2. The reset and its exact order

Let \(e_p=1\) if \(|p|\) is even and \(e_p=0\) if it is odd. Define
\[
 c_p=
 \begin{cases}q_p,&e_p=1,\\-q_p^{k_p},&e_p=0,\end{cases}
 \qquad
 d_p^T=
 \begin{cases}v_p^T,&e_p=1,\\\mathbf e_1^T,&e_p=0.\end{cases}
 \tag{6}
\]
Here \(c_p\) is a scalar, not a spectral root.

**Lemma 1.** At color zero the first nonzero Taylor coefficient is
\[
 \mathcal T_p(0;z)
  =(z-1)^{e_p}c_pv_pd_p^T
       +O((z-1)^{e_p+1}).
 \tag{7}
\]

*Proof.* Formula (3) telescopes at \(r=q_p\):
\[
                  \mathcal B_{k_p}(q_p;q_p)=q_pv_pv_p^T.
 \tag{8}
\]
For an even run, \(1-z^{-1}=(z-1)+O((z-1)^2)\), which proves
(7). For an odd run, the diagonal in (4) at \(z=1\) is
\(\operatorname{diag}(-1,0,\ldots,0)\). Since the first coordinate
of \(v_p\) is \(q_p^{k_p-1}\), its product with (8) is
\(-q_p^{k_p}v_p\mathbf e_1^T\). This also covers \(k_p=1\).
\(\square\)

Write \(k=k_a\), \(\ell=k_b\), \(s=e_a+e_b\), and
\[
 w_0=v_a\otimes v_b,\quad
 \chi=c_ac_b,\quad h^T=d_a^T\otimes d_b^T,\quad
 c^T=\mathbf e_k^T\otimes\mathbf e_\ell^T.
 \tag{9}
\]
For every color \(0\le j<N\), define
\[
 A_j(z)=\mathcal T_a(j;z)\otimes\mathcal T_b(j;z),\qquad
 \mathcal F_j(z)=
 \begin{pmatrix}A_j(z)&0\\c^TA_j(z)&1\end{pmatrix},\qquad
 P_{\rm acc}=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
 \tag{10}
\]
These are \(k\ell+1\) dimensional matrices. The exact reset is
\[
 \mathcal F_0(z)-P_{\rm acc}
  =(z-1)^s\chi
       \binom{w_0}{1}(h^T,0)+O((z-1)^{s+1}).
 \tag{11}
\]
In particular, an even run causes a zero at the reset. Applying
that zero transfer to arbitrary initial data would lose the source.

## 3. Source extraction from the full-period matrix

Form the ordered product
\[
       \mathcal M_N(z)=
           \mathcal F_D(z)\mathcal F_{D-1}(z)\cdots
                  \mathcal F_0(z).
 \tag{12}
\]
Let the actual state, including the original color-zero contribution,
be
\[
 \binom{w_D}{\zeta_D}
   =\mathcal F_D(1)\cdots\mathcal F_1(1)\binom{w_0}{1}.
 \tag{13}
\]
The exact two-run theorem says \(\mathcal Z_{a,b,N}=\kappa^{a+b}\zeta_D\).

**Theorem 2.** The first source-bearing jet of the full-period matrix is
\[
 \boxed{\quad
 \mathcal M_N(z)-P_{\rm acc}
   =(z-1)^s\chi\binom{w_D}{\zeta_D}(h^T,0)
                      +O((z-1)^{s+1}).
 \quad}                                                        \tag{14}
\]
Choose channel indices
\[
 i_a=\begin{cases}k,&e_a=1,\\1,&e_a=0,\end{cases}\qquad
 i_b=\begin{cases}\ell,&e_b=1,\\1,&e_b=0.\end{cases}
 \tag{15}
\]
Then \(h_{(i_a,i_b)}=1\), and the original source is exactly
\[
 \boxed{\quad
 \mathcal Z_{a,b,N}
   =\frac{\kappa^{a+b}}{s!\chi}
      \left[
       \frac{d^s}{dz^s}\mathcal M_N(z)\bigg|_{z=1}
      \right]_{{\rm acc},(i_a,i_b)} .
 \quad}                                                        \tag{16}
\]

*Proof.* The last column in (10) gives the identity
\(\mathcal F_j(z)P_{\rm acc}=P_{\rm acc}\) for every \(j,z\).
Consequently
\[
 \mathcal M_N(z)-P_{\rm acc}
   =\mathcal F_D(z)\cdots\mathcal F_1(z)
                        (\mathcal F_0(z)-P_{\rm acc}).
 \tag{17}
\]
Substitute (11). For its first nonzero coefficient, every other
factor is evaluated at \(z=1\), yielding (13) and (14).
Equivalently, no derivative of a later factor contributes at that
order: all lower reset coefficients vanish, while every derivative
on \(P_{\rm acc}\) is zero. Finally (15) and the source normalization
after (13) prove (16). The chosen input column is a channel column,
so \(P_{\rm acc}\) contributes zero even when \(s=0\).
\(\square\)

The three cases are as follows:

| Parities of \((|a|,|b|)\) | Jet order \(s\) | \(\chi\) |
|---|---:|---|
| odd, odd | \(0\) | \(q_a^kq_b^\ell\) |
| even, odd | \(1\) | \(-q_aq_b^\ell\) |
| odd, even | \(1\) | \(-q_a^kq_b\) |
| even, even | \(2\) | \(q_aq_b\) |

All four sign choices occur in the same formulas. At
\((a,b)=(-4,-5)\), one has \(k=2,\ell=3,s=1\),
\(\chi=-q^{-4}\), selected channel \((2,1)\), and
\[
 \mathcal Z_{-4,-5,N}
       =-\kappa^{-9}q^4
                    \mathcal M_N'(1)_{{\rm acc},(2,1)}.
 \tag{18}
\]
The powers of \(q\) and \(\kappa\) use the definitions in Section 1,
at both parities of \(N\).

## 4. Coefficient spectators and the remaining analytic question

The construction preserves an arbitrary specified diagonal color
weight \(\omega_j\): replace the bottom-left entry in (10) by
\(\omega_jc^TA_j(z)\), initialize (13) with
\((w_0,\omega_0)^T\), and retain the same \(\chi,h,s\).
The proof of (14) is unchanged. The extracted scalar is then
\[
              \sum_{j=0}^D\omega_j(M^a)_{j0}(M^b)_{j0}.
 \tag{19}
\]
The weights may themselves be holomorphic spectator functions;
the equality holds coefficientwise, including their derivatives.
This is not a claim that every geometric free boundary acts
diagonally in these colors. The full Newton arrays in (5) remain
available for other exact contractions.

For every \(z\), the matrix in (12) has the block form
\[
                \begin{pmatrix}U_N(z)&0\\v_N(z)^T&1\end{pmatrix}.
 \tag{20}
\]
Its characteristic polynomial is
\((\lambda-1)\det(\lambda I-U_N(z))\), independent of the bottom
row \(v_N(z)^T\). The source in (16) is precisely an entry of that
row or one of its derivatives. Changing the weights in (19) leaves
this characteristic polynomial unchanged while changing the source.
Therefore a characteristic identity for a cyclotomic product,
including the proved
[endpoint characteristic theorem](research_cyclotomic_endpoint_monodromy.md),
does not alone identify this source-bearing jet. A useful extension
must retain the corresponding noncentral matrix entry and its reset
order.

There is a stronger local qualification when at least one power is
even. Then \(U_N(1)=0\), so \(I-U_N(z)\) is invertible near \(1\).
Set
\[
 h_N(z)^T=v_N(z)^T(I-U_N(z))^{-1},\qquad
 S_N(z)=\begin{pmatrix}I&0\\h_N(z)^T&1\end{pmatrix}.
 \tag{21}
\]
Direct multiplication gives
\[
 S_N(z)\mathcal M_N(z)S_N(z)^{-1}
                   =\operatorname{diag}(U_N(z),1).
 \tag{22}
\]
Moreover \(S_N(1)=I\), because \(v_N(1)=0\). Thus even a
holomorphic local similarity, normalized to be the identity at the
physical point, can remove the entire accumulator row. Its derivatives
carry the source. A future full-matrix identity up to similarity must
therefore retain the marked input/output vectors and the corresponding
derivatives of its conjugator; an unmarked local conjugacy class
still loses the quantity in (16).

Equations (14)--(19) keep the coherent original color sum; they
neither replace it by absolute values nor infer its nonvanishing.
No geometric action, asymptotic leading coefficient, or general
short-component closure is proved here.

## 5. Independent clocks and the marked cyclic equation

Replace the two appearances of \(z\) in (4) by independent
parameters \(z_a,z_b\), respectively, and write
\(\mathbf z=(z_a,z_b)\). All definitions (9)--(13) extend with this
change. Define the finite-order shift
\[
             \tau\mathbf z=(Q_a z_a,Q_b z_b),\qquad \tau^N=I.
 \tag{23}
\]
In particular, \(\mathcal F_j(\tau\mathbf z)
=\mathcal F_{j+1}(\mathbf z)\), with subscripts taken modulo \(N\).
For same signs the diagonal \(z_a=z_b\) is preserved by this shift;
for opposite signs it generally is not.

**Proposition 3.** There is a holomorphic matrix
\(\mathcal R(\mathbf z)\) near \((1,1)\) such that
\[
 \begin{split}
 \mathcal M_N(\mathbf z)-P_{\rm acc}
     &=(z_a-1)^{e_a}(z_b-1)^{e_b}\mathcal R(\mathbf z),\\
 \mathcal R(1,1)
     &=\chi\binom{w_D}{\zeta_D}(h^T,0).
 \end{split}                                                    \tag{24}
\]
Consequently the complete source is the mixed reset jet
\[
 \boxed{\quad
 \mathcal Z_{a,b,N}
   =\frac{\kappa^{a+b}}{\chi}
      \left[
       \partial_{z_a}^{e_a}\partial_{z_b}^{e_b}
                  \mathcal M_N(\mathbf z)\big|_{(1,1)}
      \right]_{{\rm acc},(i_a,i_b)} .
 \quad}                                                        \tag{25}
\]
There is no factorial in (25), since \(e_a,e_b\in\{0,1\}\).
The diagonal specialization of (24) recovers (14)--(16), including
the factor \(s!\).

*Proof.* Apply Lemma 1 separately to the two factors of \(A_0\).
Then use the exact identity (17), now in two variables. The stated
divisibility is holomorphic divisibility, so partial derivatives
of smaller reset order vanish identically at the required face.
The mixed coefficient is the product of the two first nonzero
reset coefficients and the later factors evaluated at \((1,1)\).
\(\square\)

The full-period matrix obeys an identity even at the singular reset:
\[
 \boxed{\quad
     \mathcal M_N(\tau\mathbf z)\mathcal F_0(\mathbf z)
          =\mathcal F_0(\mathbf z)\mathcal M_N(\mathbf z).
 \quad}                                                        \tag{26}
\]
Indeed both sides are
\(\mathcal F_0\mathcal F_D\cdots\mathcal F_1\mathcal F_0\).
No matrix inverse or discarded endpoint term occurs in this proof.

To display the information in (26), write
\(\mathcal M_N=\left(\begin{smallmatrix}U&0\\r&1\end{smallmatrix}\right)\)
with \(r\) a row, and put \(A=A_0(\mathbf z)\). Then
\[
 \boxed{\begin{aligned}
       U(\tau\mathbf z)A&=AU(\mathbf z),\\
       r(\tau\mathbf z)A-r(\mathbf z)
                       &=c^TA\bigl(U(\mathbf z)-I\bigr).
 \end{aligned}}                                                \tag{27}
\]
The second line is the inhomogeneous transport equation for the
marked accumulator. Retaining only the first line loses the source.

For completeness the exact invertibility set follows from (3):
\[
 \begin{split}
 \det\mathcal B_k(q_p z;q_p)
       &=(q_p z)^k(1-z)^{k-1},\\
 \det\mathcal T_p(0;z)
       &=(-q_p)^k(1-z)^{|p|-1}.
 \end{split}                                                    \tag{28}
\]
One may first compute these identities away from \(z=1\) using
\(\det[C_k(r)-q_p^{-1}E_{kk}]=r^{-k}(1-r/q_p)\);
polynomial continuation supplies the reset. Thus \(A\), and hence
\(\mathcal F_0\), is invertible for generic \(\mathbf z\) near
\((1,1)\). On that set (26) is a cyclic similarity. Equation (27)
is its extension that remains valid at the physical reset.

On the open set where \(I-U\) is invertible, put
\[
        \mathfrak h(\mathbf z)=r(\mathbf z)(I-U(\mathbf z))^{-1}.
 \tag{29}
\]
Where both terms are defined, (27) gives
\[
 \boxed{\quad
       \mathfrak h(\tau\mathbf z)A=\mathfrak h(\mathbf z)-c^TA.
 \quad}                                                        \tag{30}
\]
To prove this without commuting matrices, use
\((I-U(\tau\mathbf z))A=A(I-U(\mathbf z))\), multiply its
inverse relation in the same order, and then apply the second
line of (27). If at least one power is even, the full top product
is zero at every point \(\tau^j(1,1)\), because it contains the
zero top reset factor. Hence \(\mathfrak h\) is holomorphic near the entire
finite physical orbit. Equation (30) there is a genuine finite
inhomogeneous difference identity, with (24) fixing its original
source normalization. It is not a positivity or inverse-norm bound.
At the base point, both \(r\) and \(U\) have the reset factor in
(24). Thus, when \(s>0\), \(\mathfrak h-r=rU(I-U)^{-1}\) has its square.
In particular
\[
   \partial_{z_a}^{e_a}\partial_{z_b}^{e_b}
                     \mathfrak h(1,1)=\chi\zeta_Dh^T.
 \tag{31}
\]
Here \(h^T\) is the fixed reset row from (9).
Equation (31) keeps the marked source while using the
affine equation (30).

The cyclic statements (26)--(30) concern the unweighted original
source. For fixed arbitrary color weights in (19), a clock shift
must also rotate the weight list, or the weights must themselves
be supplied equivariantly along the clock orbit. Their mixed-jet
identity (24)--(25) remains valid without that additional rule.
Likewise, for opposite signs, restricting prematurely to the
diagonal multiplier cannot be used to infer (26) in one variable.
For an explicit failure, take \(N=3,a=2,b=-2\) and put
\(Q=e^{2\pi i/3}\). On the diagonal \(z_a=z_b=z\) the one-channel
top factors are \(A_0=(z-1)^2\) and
\(A_1=A_2=z^2+z+1\). Hence
\[
 U(z)=(z^3-1)^2,\qquad
 r(z)=z^6+z^4-3z^3+z^2-3z+3.
 \tag{32}
\]
The bottom-left entry of the incorrectly asserted common-shift
intertwining would require
\(r(Qz)A_0-r(z)-A_0(U(z)-1)=0\).
Its coefficient of \(z^6\) is \(Q-1\ne0\).
The independent-clock equation (26) remains exact.

**Corollary 4 (one clock with the original sign directions).**
There is a different one-variable specialization that preserves
cyclic transport for every sign pair:
\[
   \iota(x)=(x^{\sigma_a},x^{\sigma_b}),\qquad
   \widehat{\mathcal M}_N(x)=\mathcal M_N(\iota(x)),\qquad
   \widehat A(x)=A_0(\iota(x)).
 \tag{33}
\]
It is holomorphic for \(x\) near \(1\), and
\(\iota(Qx)=\tau\iota(x)\). Hence (26)--(30) restrict to
genuine cyclic and affine transport with \(x\mapsto Qx\);
in particular,
\[
 \widehat{\mathfrak h}(Qx)\widehat A(x)
       =\widehat{\mathfrak h}(x)-c^T\widehat A(x)
 \tag{34}
\]
where the rows are defined. Set
\(\epsilon=\sigma_a^{e_a}\sigma_b^{e_b}\in\{1,-1\}\).
Then the exact original source is
\[
 \boxed{\quad
 \mathcal Z_{a,b,N}
   =\frac{\kappa^{a+b}}{s!\chi\epsilon}
       \left[
       \frac{d^s}{dx^s}\widehat{\mathcal M}_N(x)\bigg|_{x=1}
       \right]_{{\rm acc},(i_a,i_b)} .
 \quad}                                                        \tag{35}
\]
Indeed \(x^{\sigma_p}-1=\sigma_p(x-1)+O((x-1)^2)\).
Substituting into (24) proves (35) directly. At
\((-4,-5)\) its prefactor is \(+\kappa^{-9}q^4\), in contrast
to the common-multiplier prefactor in (18). These derivatives
are taken along different auxiliary curves; the original scalar
is the same.

Let \(\widehat U_N(x)\) denote the top block. Its entries are
Laurent polynomials in \(x\), and cyclic similarity holds away
from the finitely many zeros of \(\det\widehat A(x)\).
Consequently
\[
    \det(\lambda I-\widehat U_N(x))
                     \in\mathbb C[\lambda,x^N,x^{-N}].
 \tag{36}
\]
To see this, similarity gives invariance under \(x\mapsto Qx\)
on a nonempty open set, hence as a Laurent-polynomial identity.
Since \(Q\) has exact order \(N\), every nonzero Laurent exponent
in each coefficient is divisible by \(N\). Thus
\(\det(I-\widehat U_N(x))\) depends only on \(X=x^N\).
Whenever it is not identically zero, it supplies an invariant
denominator for the rational affine row. In fact the subsequent
[original source characteristic theorem](research_resonant_source_monodromy_characteristic.md)
proves that it is identically zero for every odd--odd pair:
each odd run has the same invariant eigenvalue \((-1)^{N-1}\).
For example, \(a=b=1\) has \(\widehat U_N\equiv1\).
The invariant-polynomial conclusion holds for arbitrary signed
powers, but does not identify that polynomial with a prescribed
classical curve. It also does not remove the numerator and marked
jet in (35). When \(s>0\) the denominator equals one at \(x=1\),
whereas the source jet can still be exponentially large.

For the knot cases, the
[marked Laurent numerator theorem](research_two_run_marked_laurent_numerator.md)
retains that missing row in a unique forced finite-band coefficient
system and recovers the original scalar from a marked evaluation.

## 6. The knot case has a holomorphic affine row

The original source (1) closes the literal tangle
\(R^bT(R^a)\) by the prescribed cylindrical closure \(C\).
Use the original ordered endpoints
\(0=\mathrm{BL},1=\mathrm{BR},2=\mathrm{TR},3=\mathrm{TL}\),
as in the [marked collar convention](research_rational_corridor_compression.md)
and the [two-circle family](research_two_circle_finite_exceptions.md).
The three endpoint pairings are
\[
 V=\{03,12\},\qquad H=\{01,23\},\qquad X=\{02,13\}.
 \tag{37}
\]
The through identity has pairing \(V\). An odd integral braid
interchanges \(V\) and \(X\) and fixes \(H\); an even braid fixes
all three pairings. This is the actual interchange of the two
bottom endpoints by a bottom half-twist. The prescribed physical
quarter-turn sends old endpoint \(i\) to \(i-1\bmod4\), so it
interchanges \(V,H\) and fixes \(X\). These rules give the complete
two-run table:

| \(a\bmod2\) | \(b\bmod2\) | Pairing of \(R^bT(R^a)\) |
|---:|---:|---|
| \(0\) | \(0\) | \(H\) |
| \(0\) | \(1\) | \(H\) |
| \(1\) | \(0\) | \(X\) |
| \(1\) | \(1\) | \(V\) |

No internal closed component is created: the initial through
tangle has two arcs, a braid collar only permutes their endpoints,
and a turn rotates the whole tangle. The actual cylindrical
closure adds the outside pairing \(V\). Its union with \(H\) or
\(X\) is one four-endpoint cycle, while its union with \(V\)
has two cycles. Therefore
\[
 \boxed{\quad
 C(R^bT(R^a))\text{ has one component}
       \quad\Longleftrightarrow\quad
       a\text{ or }b\text{ is even}.
 \quad}                                                        \tag{38}
\]
This argument uses the fixed outside arcs and physical endpoint
maps; it does not infer a closure from an unmarked slope alone.

The rational-slope calculation is consistent with this table.
For the original linear collar maps
\(A_n=\left(\begin{smallmatrix}1&n\\0&1\end{smallmatrix}\right)\)
and \(S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\),
\[
       A_bSA_a=
        \begin{pmatrix}b&ab-1\\1&a\end{pmatrix}.
 \tag{39}
\]
The through tangle has slope vector \((0,1)^T\), hence the tangle
slope is \((ab-1)/a\), already reduced. Its numerator is odd
exactly in the three one-component rows above. The component
proof was the explicit pairing calculation, not an appeal to a
general rational-link parity rule.

**Corollary 5.** Every knot in this literal nonzero two-run family
has \(s=e_a+e_b\ge1\). Its full top monodromy vanishes at every
physical orbit point, and the affine row in (29) is holomorphic
in neighborhoods of that orbit. Its exact source is the marked
first or second reset jet in (25) or (35). This removes the
odd--odd invertibility qualification for this knot family,
without giving an estimate or noncancellation theorem for that jet.
No analogous parity criterion for longer rational words is asserted.

## 7. Reproduction

The [finite normalization diagnostic](../experiments/check_two_run_monodromy_source_jets.py)
differentiates the full ordered product, checks its first nonzero
one-variable and mixed matrix jets, and compares the selected entry
with the original matrices for both signs and both level parities.
It also checks the independent-clock cyclic and affine equations,
the determinant formula (28), all signed-run characteristic identities
at an arbitrary complex clock, the classical two-run denominator,
and the derivative-free original source extraction from the marked
numerator. Its
[saved result](../repro/results/research-two-run-monodromy-source-jets.json)
also tests a nonconstant complex color weight. It is not an
asymptotic certificate.

The saved 110-digit run passed 224 cases at \(N=2,\ldots,9\),
covering all three jet orders and both weighted and unweighted
pairings. It also passed 128 single-run characteristic cases,
testing 320 power traces for all \(1\le |p|\le8\), 112
two-run denominator cases, and 72 derivative-free scalar extractions.
The largest relative residual was
\(5.34591726182\cdot10^{-106}\). The script differentiates the
entire ordered product directly, rather than using (14) to form
the derivative.
