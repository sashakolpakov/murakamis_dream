# Cyclic crossing walls are exact integer-degree sectors

Private written proof, 19 November 2026.

The two cross-wall periods of S have a concrete meaning: they are
the low and high integer pair-degree blocks of the original truncated
transfer. Consequently the three wall choices inside one crossing
must agree. A word with \(c\) crossings has at most \(2^c\) surviving
sectors, rather than the \(2^{3c}\) choices in its Euler-slot expansion.

Each sector also has an exact nilpotent completion. Its ordinary
Hankel period equals the complete regularized cyclic-wall period,
including P's endpoint finite parts and cyclic-pole residues. With
the original diagonal first cut fixed throughout, H's complex
meridian-collar and genuine jet bounds hold for every completed
sector. These are identities of complete periods and absolute tail
estimates. They do not identify localized densities or prove a
nonzero geometric coefficient.

The complete directs are S (cyclic sewing), P (its regularized cut
prescription), and H (actual meridian Hankel transport). The finite
residue calculation and the crossing-sector reduction are proved here.

## 1. The two paths in one actual residue fibre

Fix \(N\ge2\), \(d=N-1\), and a nonzero scalar \(a\). On two
physical heads with basis \(e_0,\ldots,e_d\), let \(J_+\) and
\(J_-\) be the truncated unit shifts and let \(S\) be cyclic raising.
Set
\[
 T=aJ_+\otimes J_-,\qquad A=aS\otimes S^{-1},\qquad
 R_A(t)=(tI-A)^{-1}.
 \tag{1}
\]
The letter S in (1) denotes a matrix; the proof-source S is cited
by its section or equation when needed. Both operators preserve the
sum of the occupations modulo \(N\). In the residue \(k\), put
\[
 h=k+1\in\{1,\ldots,N\},\qquad
 b_n=e_n\otimes e_{(k-n)\bmod N},\quad 0\le n<N.
 \tag{2}
\]
Then \(Ab_n=ab_{n+1\bmod N}\). The physical \(T\) deletes the
arrows from \(h-1\) to \(h\) and from \(N-1\) to zero. When
\(h=N\), these are the same arrow. Thus its two paths are
\([0,h-1]\) and \([h,N-1]\), with the latter empty at \(h=N\).
Their exact integer pair totals are respectively \(k\) and \(k+N\).
Write \(\Pi_{h,0}\) and \(\Pi_{h,1}\) for their diagonal projectors.

Put \(z=a/t\), interpret \(b_h=b_0\) if \(h=N\), and define S's
two cross-wall matrices in their actual order:
\[
 \begin{split}
 C_{h,1}(t)&=R_A(t)b_0z^{N-h}b_h^t A R_A(t),\\
 C_{h,0}(t)&=R_A(t)b_hz^h b_0^t A R_A(t).
 \end{split}
 \tag{3}
\]
The transpose here is the coordinate row, not a Hermitian dual.
S(2)--(4) says that the other three terms of the resolvent sewing
formula are holomorphic at zero. We will identify the two surviving
terms separately.

**Finite residue identity.** For every germ
\(f(t)=\sum_{\nu\ge0}f_\nu t^\nu\) holomorphic at zero, and a
sufficiently small positive circle \(\gamma\) with radius less
than \(|a|\),
\[
 \boxed{\quad
 \frac1{2\pi i}\int_\gamma f(t)C_{h,b}(t)\,dt
       =f(T)\Pi_{h,b},\qquad b=0,1,
 \quad}                                                   \tag{4}
\]
where \(f(T)=\sum_{\nu=0}^{d}f_\nu T^\nu\).

To prove it, use the convergent series at zero
\[
 R_A(t)=-\sum_{p\ge0}t^p A^{-p-1},\qquad
 A R_A(t)=-\sum_{q\ge0}t^q A^{-q}.
 \tag{5}
\]
For the high wall in (3), a residue can occur only when
\[
 p+q+\nu=N-h-1.
 \tag{6}
\]
If \(h=N\), this is impossible and the high wall has zero period.
Otherwise (6) bounds \(p,q\le N-h-1\), so no cyclic ambiguity
remains in
\[
 A^{-p-1}b_0=a^{-p-1}b_{N-1-p},\qquad
 b_h^tA^{-q}=a^{-q}b_{h+q}^t.
 \tag{7}
\]
Its output \(u=N-1-p\) and input \(v=h+q\) satisfy
\(h\le v\le u<N\), \(u-v=\nu\), and the scalar is
\(a^{N-h-p-q-1}f_\nu=a^{u-v}f_{u-v}\).
Conversely every such pair \((u,v)\) occurs exactly once, with
\(p=N-1-u\), \(q=v-h\). This is precisely \(f(T)\Pi_{h,1}\).

For the low wall, the residue condition is
\(p+q+\nu=h-1\). Now the output and input are
\(u=h-1-p\) and \(v=q\), with \(0\le v\le u<h\), and the
same scalar is \(a^{u-v}f_{u-v}\). Every such pair occurs once.
This calculation remains valid at \(h=N\): the cyclic symbol
\(b_h=b_0\) in (3) gives the displayed representatives without
an extra wrap term. It proves (4) also at the coincident wall.
All sums contributing to a residue are finite.

Summing over the residue fibres gives the physical projectors
\[
 \Pi_0=\mathbf1_{J_1+J_2\le d},\qquad
 \Pi_1=\mathbf1_{J_1+J_2\ge N},\qquad \Pi_0+\Pi_1=I.
 \tag{8}
\]
Here \(J_ie_j=je_j\); the inequalities use integer degree, not
degree modulo \(N\). Reversing the transfer exchanges the two
heads and leaves both projectors unchanged. No parity or primality
assumption entered the proof.

## 2. Nilpotent completion retains the cyclic-pole currents

Let \(\operatorname{pp}_0\) denote the negative Laurent part at zero.
Testing (4) on every monomial \(f(t)=t^\nu\) proves entrywise
\[
 \operatorname{pp}_0 C_{h,b}(t)
    =\sum_{\nu=0}^{d}t^{-\nu-1}T^\nu\Pi_{h,b}
    =(tI-T)^{-1}\Pi_{h,b}.
 \tag{9}
\]
Thus the difference
\[
 D_{h,b}(t)=C_{h,b}(t)-(tI-T)^{-1}\Pi_{h,b}
 \tag{10}
\]
is holomorphic at zero. This is an exact change of completion for
the same small-circle functional. The second term has no nonzero
finite pole; the first generally has the cyclic poles \(t^N=a^N\).
They are not equal rational matrices.

For the actual root transfers in H, \(|a|=1\), and the scalar germ
is one of the marked inverse cyclic dilogarithms
\[
 \mathscr A_\epsilon(t)=
       \prod_{j=1}^{N-1}(1-Q^{\epsilon j}t)^{-j/N},
 \qquad Q=e^{2\pi i/N},\quad \mathscr A_\epsilon(0)=1.
 \tag{11}
\]
P's regularized Hankel formula applies to \(C_{h,b}\) and to
\(D_{h,b}\). Both have at most double nonzero poles and are
\(O(t^{-1})\) at infinity. Its prescribed functional is the sum
of the marked bank finite parts **minus** the residues at unramified
cyclic poles. At a branch endpoint of exponent \(-u\), it subtracts
the two Laurent terms \(b_{-2}x^{-2},b_{-1}x^{-1}\) and retains the
finite constants \(-b_{-2}/(u+1)-b_{-1}/u\).

Apply that formula to (10). Its original small-circle period is zero,
because \(D_{h,b}\) is holomorphic there. The result is exactly
\[
 \boxed{\quad
 \mathcal H^{\rm reg}_{\epsilon}[C_{h,b}]
       =\mathcal H^{\rm ord}_{\epsilon}
                         [(tI-T)^{-1}\Pi_{h,b}].
 \quad}                                                   \tag{12}
\]
On the right, the ordinary Hankel integral converges at every branch
endpoint and infinity, as in H. Thus (12) incorporates the cyclic-pole
currents into the nilpotent completion. It does not omit them from
the left side. It holds at odd, even, and composite levels, including
the collisions of cyclic poles with branch endpoints. P's marked
sheet and cut-arc convention is retained at infinity.

The independent slot variables permit repeated use of (12) inside
any fixed ordered tensor contraction. Equivalently, start from its
compact product of small circles, apply (9) one variable at a time,
then use the proved cut prescriptions. This argument does not assume
absolute convergence of a raw, unregularized cyclic-wall integral.
Nor does (12) identify restrictions to a chosen radial subregion or
geometric window: the completion change can redistribute its currents.

## 3. Three slot choices reduce to one choice per crossing

Use H's root factorization of a physical crossing, with
\(q=e^{\pi i/N}\), \(x_0=-q^{-1}\), and \(F_a=(Q;Q)_a\):
\[
 \begin{split}
 C&=F_2u_N(T_-)F_1F_2^{-1},&
 C^{-1}&=F_2F_1^{-1}v_N(T_-)F_2^{-1},\\
 \widehat R_0^+&=CDu_N(T_+)C^{-1},&
 \widehat R_0^-&=Cv_N(T_+)D^{-1}C^{-1}.
 \end{split}
 \tag{13}
\]
The matrices \(F_i\) and \(D\) are diagonal; \(T_\pm\) are the
opposite truncated transfers. The hat removes only the common
crossing scalar. As defined in H,
\(u_N(t)=\sum_{a<N}t^a/F_a\) and
\(v_N(t)=\sum_{a<N}(-1)^aQ^{a(a-1)/2}t^a/F_a\).
Each signed crossing has three transfer slots and six factorial slots.
Every one of its factors preserves the same integer pair degree,
so every factor commutes with both projectors (8).

In S's five-term sewing expansion, any term having even one pure
cyclic or diagonal sewing slot has zero complete period: integrate
that variable first, whose integrand is holomorphic inside its small
circle. All other slots and the chosen coupon are independent of it.
Thus a surviving word must choose a cross wall at every transfer slot.

In the all-inverse realization, a \(u_N(T)\) slot uses
\(\mathscr A_-(t)(tI-Q^{-1}T)^{-1}\); the scalar rotation changes
neither its two paths nor its projectors. By (4), choosing wall
\(b\) at any slot replaces that slot's integrated operator by
\(u_N(T)\Pi_b\) or \(v_N(T)\Pi_b\), respectively.
For a three-slot choice \((b_1,b_2,b_3)\), its block period is therefore
\[
              \widehat R_0^{\pm}\Pi_{b_1}\Pi_{b_2}\Pi_{b_3}.
 \tag{14}
\]
It vanishes unless all three choices agree, in which case it is
\(\widehat R_0^{\pm}\Pi_b\). Factorial integrations may be performed
before or after this calculation, since they are independent and
their matrix kernels are diagonal. In the nilpotent completion the
projectors commute already with those kernels and the transfer
resolvents, so mismatched choices vanish pointwise in that completed
network. This last statement is not asserted for the raw cyclic walls.

For the true meridian family, put \(M=e^\mu\) and \(x=-M/q\).
H(3) expresses each \(R_i^{\pm}(M)\) as its root crossing between
the literal moving diagonal frames and \(M^{\mp(J_i+J_{i+1})}\),
with \(\kappa(M)^{\pm1}\) retained. All these matrices commute
with \(\Pi_{i,b}\), the projector (8) on that adjacent pair.
Consequently the surviving block period is exactly
\[
                         R_i^{\pm}(M)\Pi_{i,b}.
 \tag{15}
\]
This uses fixed root transfer variables and fixed root cyclic poles;
no off-root strict Euler factorization is differentiated.

Let a word act in the order
\(W_\beta=R_{i_c}^{\sigma_c}\cdots R_{i_1}^{\sigma_1}\),
\(\sigma_\ell\in\{+1,-1\}\). Define its degree-sector operator
\[
 W_{\beta,\mathbf b}(M)=
       (R_{i_c}^{\sigma_c}(M)\Pi_{i_c,b_c})\cdots
       (R_{i_1}^{\sigma_1}(M)\Pi_{i_1,b_1}),
 \qquad \mathbf b\in\{0,1\}^c.
 \tag{16}
\]
Then the complete all-wall period is exactly
\[
                        W_\beta(M)=\sum_{\mathbf b}W_{\beta,\mathbf b}(M).
 \tag{17}
\]
More than an insertion of \(I=\Pi_0+\Pi_1\), (14)--(16) identify
which original cyclic-wall periods give these terms and prove that
every other three-slot pattern has zero complete period. Each
surviving term has the nilpotent completion (12).

There is no claim that projectors for one pair commute through a
crossing on an overlapping pair. The order in (16) stays fixed.
In literal occupation paths, \(b_\ell\) is the indicator that the
input sum at crossing \(\ell\) is at least \(N\); its output sum
is identical. Thus the sectors partition the original capped flow.

## 4. The original pointed source and sectorwise meridian tails

Fix the original coupon before splitting any crossing. For \(m\)
heads and writhe \(w=\sum\sigma_\ell\), set
\[
 \mathcal P_{\mathbf b,N}(M)=\Xi_N(M)
  \operatorname{Tr}[(P_0\otimes K_{\rm r}(M)^{1-N})
                                  W_{\beta,\mathbf b}(M)],
 \qquad P_0=|0\rangle\langle0|.
 \tag{18}
\]
The external line \(\Xi_N\) is unchanged in every term. Equations
(12),(17) give \(\mathcal P_N=\sum_{\mathbf b}\mathcal P_{\mathbf b,N}\)
as actual meridian germs, including all their true fixed-\(q\) jets.
These sectors need not be total \(E,F\) intertwiners: pair raising
or lowering crosses the threshold in (8). Scalar-cut identities
therefore cannot replace (18) by a different coupon sectorwise.

More explicitly, let \(E_{\rm pair}\) and \(F_{\rm pair}\) be the
actual total lowering and raising operators on that pair. They lower
and raise \(J=J_i+J_{i+1}\) by one, respectively, including their
physical endpoint zeros. Directly on each integer-degree subspace,
\[
 [E_{\rm pair},\Pi_0]=-E_{\rm pair}\mathbf1_{J=N},\qquad
 [F_{\rm pair},\Pi_0]=F_{\rm pair}\mathbf1_{J=d}.
 \tag{18a}
\]
For instance, only an input of degree \(N\) is lowered from outside
the low sector into it. The corresponding high-sector commutators
have the opposite signs. Thus for a scalar mark \(\zeta\),
\[
 \begin{split}
 [E_{\rm pair},\Pi_0+\zeta\Pi_1]
       &=(\zeta-1)E_{\rm pair}\mathbf1_{J=N},\\
 [F_{\rm pair},\Pi_0+\zeta\Pi_1]
       &=(1-\zeta)F_{\rm pair}\mathbf1_{J=d}.
 \end{split} \tag{18b}
\]
These are retained threshold currents, not errors in the sector
construction. Their cancellation when \(\zeta=1\) does not make
the separately marked sectors intertwining sources.

Write \(\mathcal E_N=\Xi_N\kappa(M)^w\) and define the stripped
sector directly by removing the crossing scalars. Apply H's
all-inverse fixed-bank construction to the nilpotent completion
of (16). It has the same \(s=9c\) variables as H, with constant
orthogonal projectors inserted in their literal positions.
Their norm is one; they introduce no poles or meridian derivatives.
All H's moving frames remain at their original stages.

For \(0<\eta<\eta'<\pi\), put \(M=e^{u/N}\), \(|u|\le\eta'\).
The complete rational source of each sector obeys, uniformly in
\(\mathbf b\),
\[
 |\mathcal R_{\mathbf b,N}(\boldsymbol\rho,\boldsymbol j;u)|
             \le C(N+1)^B\prod_{\ell=1}^{s}\rho_\ell^{-1}.
 \tag{19}
\]
Indeed H bounds the moving diagonals and inverses by powers of \(N\),
the actual coupon by \(e^{(m-1)\eta'}N^{m-1}\), each transfer or
direct-factorial kernel by \(N/\rho\), and each inverse-factorial
kernel by \(1/\rho\). Inserting norm-one projectors changes none
of these estimates. Constants depend on the fixed word and collar.

Let \(\widehat{\mathcal P}^{\rm nil}_{\mathbf b,N,tail}(R,u)\)
denote the ordinary completed Hankel integral restricted to
\(\max\rho_\ell\ge R\), \(R\ge1\). Define
\[
 G_j=\frac{|(Q;Q)_j|}{N^{j/N+1/2}},\qquad
 c_N=\frac{(N-1)(N-2)}{4N}.
 \tag{20}
\]
H's integrable endpoint envelope and Cauchy's formula on the
buffered \(u\)-disk give, for every fixed integer \(k\ge0\),
\[
 \sup_{|u|\le\eta}
 |\partial_\mu^k\widehat{\mathcal P}^{\rm nil}_{\mathbf b,N,tail}(R,u)|
 \le \frac{k!N^k}{(\eta'-\eta)^k}
       C(N+1)^B sR^{-c_N}\Big(\sum_{j=1}^{N-1}G_j\Big)^s.
 \tag{21}
\]
The full absolute integral has the analogous bound without
\(sR^{-c_N}\). The banks and endpoint exponents do not depend on
\(u\), so the same envelope justifies holomorphy and differentiation
under the integral. These are genuine meridian derivatives of the
stripped family associated with (18), including its pivot and moving
frames, rather than derivatives of a root-only symbol. The external
line is restored by its full product rule below.

Writing \(v_3\) for the regular ideal tetrahedron volume, H's
uniform estimate for \(G_j\) proves
\[
 \limsup_{N\to\infty}\frac1N\log
 \sup_{|u|\le\eta}
 |\partial_\mu^k\widehat{\mathcal P}^{\rm nil}_{\mathbf b,N,tail}(R,u)|
       \le\frac{9cv_3}{2\pi}-\frac14\log R.
 \tag{22}
\]
The bound is uniform over the finite \(2^c\) sectors and also bounds
their sum of absolute tail values. For the standard zero-framed
source, H(16) gives \(\mathcal E_N=x^{dw}\), bounded on the collar,
with derivative \((dw)^a x^{dw}\) of order \(a\). Thus (22) holds
for its full sector jets. H's explicit normalized dimension lines
remain permitted; an additional prescribed line retains its exact
product rule and needs its stated buffered subexponential bound.
At \(N=2\), \(c_N=0\); (22) is a large-level statement. For an
empty word there is one sector and no radial tail.

The superscript in (21)--(22) is essential. These tails belong to
the nilpotent completion. Their estimate is not transferred to a
partial raw cyclic-wall bank by equality of complete periods.

## 5. The actual coherent projector kernels

There is a useful complex domain on which one sector projector has
an identity-like normalized kernel. There are also regular complex
points where both normalized kernels grow exponentially and cancel.
Both facts follow directly from the finite binomial coefficients.

For two heads put \(v_i=z_iw_i\), where \(z_i,w_i\) are the ordinary
binomial coherent variables, and assume \(1+v_i\ne0\). Their identity
kernel is \(I_N=(1+v_1)^d(1+v_2)^d\). Inserting the diagonal
projectors (8) and dividing by this kernel gives exactly
\[
 L_N(v_1,v_2)=\frac{\displaystyle\sum_{a+b\le d}
             \binom da\binom db v_1^av_2^b}{I_N},\qquad
 H_N(v_1,v_2)=1-L_N(v_1,v_2).
 \tag{23}
\]
These are kernels of the actual finite projectors, without an
interpolation of their occupation thresholds.

Write \(x=|v_1|\), \(y=|v_2|\), and
\[
 \Gamma(v_1,v_2)=
     \frac{(\sqrt x+\sqrt y)^2}{|1+v_1|\,|1+v_2|}.
 \tag{24}
\]
If \(xy<1\), then
\[
                  |H_N|\le\sqrt{xy}\,\Gamma^d;
 \qquad
 xy>1\quad\Longrightarrow\quad |L_N|\le\Gamma^d.
 \tag{25}
\]
For the first bound use any \(R>1\): on the high range
\(a+b\ge d+1\), \(R^{-a-b}\le R^{-d-1}\), whence
\[
 |H_N|\le R^{-1}
   \left[\frac{(1+Rx)(1+Ry)}{R|1+v_1||1+v_2|}\right]^d.
 \tag{26}
\]
For \(0<R<1\), the low range instead gives the same bound for
\(|L_N|\) without the initial \(R^{-1}\). Choose
\(R=(xy)^{-1/2}\); the bracket becomes \(\Gamma\), proving
(25) when \(xy\ne0\). If \(xy=0\), the high kernel vanishes
identically, so the first conclusion holds by continuity.

Consequently on every compact subset of
\(\{\Gamma<1,\ xy<1\}\), \(L_N=1+O(\gamma^d)\), and on
every compact subset of \(\{\Gamma<1,\ xy>1\}\),
\(H_N=1+O(\gamma^d)\), for some \(\gamma<1\). The same estimates
hold for every fixed holomorphic derivative of the exponentially
small difference. Indeed the strict inequalities admit a fixed
complex neighborhood with \(\Gamma\le\gamma<1\); (25) there
and Cauchy's formula prove the derivative bounds. This is a
statement about a single actual kernel, not a rule for multiplying
normalized symbols in an unevaluated network.

The chamber condition is substantive. Set \(v_1=v_2=v\) and write
\(H_d(v)=H_N(v,v)\). Vandermonde's finite binomial identity gives
\[
 H_d(v)=\frac{\binom{2d}{d}v^d}{(1+v)^{2d}}
                 \sum_{j=1}^d R_{d,j}v^j,\qquad
 R_{d,j}=\frac{\binom{2d}{d+j}}{\binom{2d}{d}}
         =\prod_{\ell=1}^j\frac{d-\ell+1}{d+\ell}.
 \tag{27}
\]
Here \(0\le R_{d,j}\le1\) and
\[
 0\le1-R_{d,j}
     \le\sum_{\ell=1}^j\frac{2\ell-1}{d+\ell}
     \le\frac{j^2}{d}.
 \tag{28}
\]
For every \(\rho<1\), summing this error against \(\rho^j\)
and bounding the omitted geometric tail proves uniformly on
\(|v|\le\rho\) that
\(\sum_{j=1}^d R_{d,j}v^j=v/(1-v)+O(d^{-1})\).
The elementary central-binomial estimate
\(\binom{2d}{d}=4^d(\pi d)^{-1/2}(1+O(d^{-1}))\) therefore gives
\[
 H_d(v)=\frac{v}{1-v}\frac1{\sqrt{\pi d}}
       \left[\frac{4v}{(1+v)^2}\right]^d
       (1+O(d^{-1}))
 \tag{29}
\]
uniformly on every compact subset of \(0<|v|<1\). The relative
error is legitimate because \(v/(1-v)\) is a unit there.

For a concrete open counterdomain put
\[
 u=\frac14+i,\qquad v=\frac{u}{1-u}=\frac{-13+16i}{25}.
 \tag{30}
\]
Then \(|v|=\sqrt{17}/5<1\), \(u=v/(1+v)\), and
\(\operatorname{Re}(u+u)=1/2<1\). Nevertheless
\[
 \frac{4v}{(1+v)^2}=4u(1-u)=\frac{19}{4}+2i,
 \qquad \left|\frac{4v}{(1+v)^2}\right|=\frac{5\sqrt{17}}4>1.
 \tag{31}
\]
Equations (29)--(31) show exponential growth of both \(H_N\) and
\(L_N=1-H_N\), whose sum remains exactly one. The same conclusion
holds uniformly near this point within the diagonal family
\(v_1=v_2\), by (29). Even an off-unit
limiting Cartan symbol does not exclude this behavior: the literal
one-head normalized kernel is
\[
 x_0\left(\frac{1+Q^{-1}v}{1+v}\right)^d
           =-\exp(-2\pi i u)(1+O(N^{-1})),
 \tag{32}
\]
uniformly on fixed incidence-free compact sets. This follows by
summing \(\binom da Q^{-a}v^a\) and expanding the fixed compact
ratio; at (30) its limiting modulus is \(e^{2\pi}\).
Equation (32) is a coherent-kernel limit, not an off-grid operator
identity or an identification of a central power. No assertion is
made that (30) represents a faithful geometric representation.

## 6. What the reduction does and does not simplify

If \(f(0)\ne0\), \(f(T)\) is invertible on each nonempty path.
In particular the Euler germs have constant term one, so the two
integrated branches on a full pair have ranks
\[
               \operatorname{rank}\Pi_0=\frac{N(N+1)}2,
       \qquad \operatorname{rank}\Pi_1=\frac{N(N-1)}2.
 \tag{33}
\]
The boundary vectors in (3) therefore do not localize the integrated
crossing to a thin endpoint or a rank-one state. The reduction removes
redundant wall histories and supplies ordinary convergent contours
for the remaining actual degree sectors. It leaves the coupled
occupation-flow sum and its original pivotal phases intact.
The physical norm-one projectors do not imply a uniformly bounded
normalized coherent symbol at an arbitrary complex point.

No determinant formula, positivity, geometric cycle coefficient,
or arbitrary-short-component lower bound follows. No asymptotic
bound on a separate reduced axis sample is inferred from (18).
The conclusions concern the specified original source, its exact
sectors and completed absolute meridian tails, together with the
single-projector kernel estimates of Section 5.

## Complete proof-source pins

* S: `notes/exact_quantum_quad_source_transport.md` (318 lines),
  SHA256 `7f88f3a12212acacfce7e96abb6a1440be93ba507ba7225d73650435a93fc474`.
* P: `notes/cyclic_sewing_regularized_cut_cycle.md` (212 lines),
  SHA256 `b61b7d077e183c91c023de8ff23700796a7695521c692af06e548910698982b5`.
* H: `notes/research_actual_meridian_hankel_transport.md` (271 lines),
  SHA256 `e50f4257e3464863167d8a04c060753d937921d27c551d8ee18f882add1111e9`.

All three complete directs were freshly whole-read nontruncated in
this author sequence. Only written mathematics and text/hash operations
were used. Frozen and public files were not edited.
