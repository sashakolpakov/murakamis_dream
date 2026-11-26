# Laurent resolution of the canonical Borel source at an Alexander node

Private written proof, 18 November 2026.

The meromorphic loop coefficients impose more compatibility than a generic
analytic shift equation. This note uses that compatibility to resolve every
transverse Borel jet into a finite Laurent space. It proves a convergent
weighted resolution, a sharper continuation domain, and an exact second
exceptional restriction. It does not identify the full moving singularity
or a geometric representation component.

## 1. Source and statements

Retain the actual source and all hypotheses of [J]. Thus
\[
 z=Y-\alpha,\quad r=\Delta_K'(\alpha)^{-1},\quad
 A=\tfrac12\alpha^2P_{LL}(\alpha,1),\quad
 B=\alpha P_{YL}(\alpha,1),\quad \eta_*=\frac B{2A},
 \tag{1}
\]
where \(\alpha\ne0,1\) is a simple Alexander root and \(A B\ne0\).
The canonical germ is
\[
 b(z,\eta)=\sum_{k\ge0}b_k(\eta)z^k
   =\sum_{j\ge0}z^{2j+1}W_j(\alpha+z)\frac{\eta^j}{j!},
 \qquad b_0(\eta)=r(1-\eta/\eta_*)^{-1/2}.
 \tag{2}
\]
Choose \(s=(1-\eta/\eta_*)^{1/2}\) with \(s=1\) at \(\eta=0\).
For \(k\ge0\), define the \(2k+1\)-dimensional space
\[
 \mathcal V_k=
 \operatorname{span}\{s^{-1},s^{-3},\ldots,s^{-(2k+1)}\}
       \mathbin{\oplus}\mathbb C[s]_{\le k-1};
 \tag{3}
\]
the polynomial summand is zero when \(k=0\).

**Theorem.** Every canonical coefficient \(b_k\) belongs to
\(\mathcal V_k\). In particular no transverse coefficient has a
logarithm at \(s=0\). There are constants \(C,D>0\) such that the sum
of the absolute values of its Laurent coefficients is at most \(CD^k\).
Consequently
\[
 |b_k(s)|\le CD^k
       \max\{|s|^{k-1},|s|^{-2k-1}\}.
 \tag{4}
\]
The same source therefore continues jointly on the two-sheeted domain
\[
 q(z,s):=D|z|\max\{|s|,|s|^{-2}\}<1,\qquad s\ne0,
 \tag{5}
\]
with
\[
 |b(z,\eta)|\le\frac{C}{|s|(1-q(z,s))}.
 \tag{6}
\]
Constants can be enlarged without changing these assertions.

Both lifts \(s=\pm1\) of \(\eta=0\) are regular in this continuation.
On any fixed annulus around \(\eta_*\), for sufficiently small \(z\),
the cluster monodromy has order two and is nontrivial. This describes
monodromy around the cluster, not its individual singular points.

For the original Borel variable \(\xi=z^2\eta\), put
\[
 w=zs,\qquad w^2=z^2-\xi/\eta_*.
 \tag{7}
\]
There is a holomorphic function \(H(z,w,u)\) near the origin, with
\(H(0,0,0)=r\), such that the continued original Borel transform is
\[
 \widehat{\mathscr W}(z,\xi)
 :=\mathcal B_h\mathscr W(\alpha+z,\xi)
 =\frac1w H\left(z,w,\frac{z^3}{w^2}\right).
 \tag{8}
\]
This is initially the original germ, and subsequently its specified
continuation. It holds where the displayed arguments are sufficiently
small and \(w\ne0\). In particular it supplies a small fixed cutoff
in \(\xi\), uniformly as \(z\to0\), outside an explicitly controlled
inner region.

## 2. Exact coefficient equation and Laurent closure of the forcing

The complete source [J] supplies
\[
 \theta=\eta\partial_\eta,\qquad I f=\int_0^\eta f(\zeta)\,d\zeta,
 \qquad P_\ell(t)=\prod_{i=1}^{\ell}(t-i),
 \tag{9}
\]
with the canonical primitives and the exact hierarchy
\[
 \mathcal L_k b_k=F_k,\qquad
 \mathcal L_k b=(k-2\theta)
       \{Bb+A I[(k-1-2\theta)b]\}.
 \tag{10}
\]
Here \(F_0=0\). Every lower term in \(F_k\), with its sign and scalar
coefficient retained, is a multiple of
\[
 I^aP_\ell(p-2\theta)b_p,\quad
 a=n-1,\quad 0\le\ell\le n,\quad p=k-\sigma\ge0,
 \quad \sigma=2a-\ell+v\ge1,\quad v\ge0.
 \tag{11}
\]
Only finitely many terms occur at fixed \(k\). The source coefficients
are the literal \(a_{n\ell}(z)\) of [J], not new free data.

In the \(s\)-coordinate,
\[
 \theta=\frac{s^2-1}{2s}\partial_s,\qquad
 I(s^m)=-\frac BA\,\frac{s^{m+2}-1}{m+2}
                         \quad(m\ne-2).
 \tag{12}
\]
Laurent polynomials with only odd negative powers remain of that form
under \(\theta\) and \(I\). An even nonnegative power cannot acquire
a negative power under \(\theta\), since its constant term differentiates
to zero. In particular the excluded exponent \(-2\), which would
produce a logarithm under \(I\), never occurs.

Suppose \(b_p\in\mathcal V_p\). Applying \(P_\ell(p-2\theta)\) raises
its pole order by at most \(2\ell\). Each primitive lowers a remaining
pole order by two. Thus the pole order of (11) is at most
\[
 \max(2p+2\ell-2a+1,0)\le2p+3\le2k+1.
 \tag{13}
\]
Integration constants are ordinary polynomials and create no pole.

The degree at infinity requires the full operator, rather than a
bound on its individual factors. The exact commutation identity is
\[
 I^aP_\ell(p-2\theta)
       =P_\ell(p+2a-2\theta)I^a.
 \tag{14}
\]
The Laurent polynomial \(I^a b_p\) has degree at infinity at most
\(p+2a-1\). Indeed the integrated terms have degree at most
\(p-1+2a\), while the polynomial integration constants have degree
at most \(2a-2\).

At infinity this Laurent polynomial has a convergent Laurent expansion
in \(\sqrt\eta\), with integer degrees bounded above by \(p+2a-1\).
On degree \(d\), \(2\theta\) acts exactly by \(d\).
The factor in (14) therefore annihilates every degree
\[
 p+2a-\ell,\ldots,p+2a-1.
 \tag{15}
\]
This is an exact finite-band cancellation, including off-diagonal
terms in the \(s\)-basis. The result has degree at infinity at most
\[
 p+2a-\ell-1=k-v-1\le k-1.
 \tag{16}
\]
Together with (13) and preservation of the negative-power parity,
this proves \(F_k\in\mathcal V_k\) whenever the lower coefficients
belong to their stated spaces.

## 3. The actual meromorphic compatibility removes the only resonance

For clarity, the leading operator preserves precisely the same space.
For an allowed monomial \(s^m\), put
\[
 G=(B-2A\eta)b+A(k+1)Ib.
 \tag{17}
\]
For \(b=s^m\), direct use of (12) gives
\[
 \mathcal L_k(s^m)=B\left[
 \frac{(m+1-k)(k-m-2)}{m+2}s^{m+2}
 +(m+1-k)s^m+\frac{k(k+1)}{m+2}\right].
 \tag{18}
\]
If \(m=k-1\) or \(m=k-2\), the possible excessive degree cancels.
For \(m=-1\), the possible excessive \(s\)-term cancels at \(k=0,1\).
All other exponents in (18) lie in \(\mathcal V_k\).
Thus \(\mathcal L_k:\mathcal V_k\to\mathcal V_k\).

To count its kernel, write the inverse Borel series as
\(\sum_{j\ge0}a_j\varepsilon^j\). Equation (10), coefficient by
coefficient, is
\[
 (k-2j)\{B a_j+A(k-2j+1)a_{j-1}\}
                       =j![\eta^j]F_k,\qquad a_{-1}=0.
 \tag{19}
\]
For odd \(k\), a homogeneous analytic germ has all \(a_j=0\).
Hence the square map on \(\mathcal V_k\) is injective and therefore
surjective.

Let \(k=2m>0\). An analytic homogeneous germ has exactly one free
coefficient, at \(j=m\). This kernel is already represented inside
\(\mathcal V_k\). To see it explicitly, take \(G=\eta^m\) and solve
\[
 \left(s^{-(k-1)}b\right)'=\frac{G_s}{B s^{k+1}},
 \qquad b(1)=0.
 \tag{20}
\]
Since \(G=\eta_*^m(1-s^2)^m\), the integrand is a linear combination
of \(s^{2j-2m}\), \(0\le j<m\). These exponents are even and never
\(-1\). After integration and multiplication by \(s^{2m-1}\),
the result is a polynomial of degree at most \(k-1\).
It is nonzero; (20) and its value at \(s=1\) ensure that its \(G\)
is exactly (17), so it is indeed a kernel vector.

The image consequently has codimension one. By (19) it lies in the
kernel of
\[
                 \lambda_k(F)=[\eta^{k/2}]F.
 \tag{21}
\]
This functional is nonzero on \(\mathcal V_k\): its value on \(s^{-1}\)
is a nonzero binomial coefficient times \(\eta_*^{-k/2}\).
Thus (21) is the entire cokernel condition.

The actual canonical coefficients in (2) exist as analytic Borel germs.
Their power-series coefficients come from the original \(W_j\),
which are meromorphic at \(\alpha\) with the stated pole bound.
Thus no logarithm in \(z\) is available to solve a resonant coefficient
equation. Applying their actual
identity (19) gives \(\lambda_k(F_k)=0\).
Therefore a solution in \(\mathcal V_k\) exists. At even \(k\),
choose its one kernel coefficient to equal the canonical coefficient
at \(j=k/2\); at odd \(k\) there is no choice. Equation (19) then
identifies every Taylor coefficient with the canonical one.
Starting with \(b_0=r/s\), induction proves (3) for all \(k\).
The compatibility here uses the actual meromorphic source, not merely
the existence of an analytic quantum operator.

## 4. Exponential coefficient bounds and balanced continuation

The joint initial germ in [J] bounds \(|b_k(s)|\le C_0D_0^k\)
on a fixed small closed disk about \(s=1\).
By (3),
\[
                 Q_k(s):=s^{2k+1}b_k(s)
 \tag{22}
\]
is a polynomial of degree at most \(3k\). It has an exponential
bound in \(k\) on the same disk. Cauchy's bounds on its coefficients
in powers of \(s-1\), followed by the finite binomial translation to
powers of \(s\), bound the sum of their absolute values by \(CD^k\).
Both the disk-radius cost raised to \(3k\) and the binomial sum are
exponential, not factorial, in \(k\).
These are exactly the Laurent coefficients of \(b_k\), proving (4).

Summing (4) proves (5)--(6). This sum agrees with the initial germ;
uniqueness of analytic continuation identifies it with the source
of [J] wherever their domains meet. For small fixed \(z\), the
allowed \(s\)-region is an annulus containing \(s=1\).

There are two useful descriptions of the resulting resolution.
First,
\[
 s\,b(z,\eta)=F\left(s,\frac z{s^2}\right),\qquad
 F(s,u)=\sum_{k\ge0}Q_k(s)u^k,
 \tag{23}
\]
where \(F\) is holomorphic near \((0,0)\).
Second, decompose the exact Laurent polynomials as
\[
 b_k(s)=\sum_{j=0}^k c_{kj}s^{-2j-1}
                    +\sum_{m=0}^{k-1}d_{km}s^m.
 \tag{24}
\]
The function in (8) is explicitly
\[
 H(z,w,u)=
 \sum_{k\ge0}\sum_{j=0}^k c_{kj}z^{k-j}u^j+
 \sum_{k\ge1}\sum_{m=0}^{k-1}d_{km}z^{k-m-1}w^{m+1}.
 \tag{25}
\]
The coefficient bounds prove convergence on a fixed polydisk.
Substitution of \(u=z^3/w^2\) gives (8) term by term.
Notice that (5) becomes
\[
                 D\max\{|w|,|z|^3/|w|^2\}<1.
 \tag{26}
\]
This is a convergent resolution of a region, not a location theorem
for all singularities inside the omitted region.

The even part in \(s\) of (24) is an ordinary polynomial of degree
at most \(k-1\). Its sum is jointly holomorphic across \(s=0,z=0\)
and is even in \(s\), hence holomorphic in \(\eta\) there.
The odd part carries the monodromy. Two circuits around \(\eta_*\)
return \(s\) to itself, exactly, in any fixed annulus for small \(z\).
One circuit is nontrivial since at \(z=0\) its difference is
\(-2r/s\). The points \(s=\pm1\) are regular by the same convergent
series. No individual moving singularity has been deduced from this
cluster statement.

For a precise fixed cutoff, choose \(R>2|\eta_*|+1\) and a sufficiently
small constant \(\xi_0>0\). Uniformly on
\[
                 R|z|^2\le|\xi|\le\xi_0
 \tag{27}
\]
for \(z\ne0\), one has \(|w|^2\asymp|\xi|\) and
\(|z|^3/|w|^2\le C|z|/R\). Thus, for all sufficiently small \(z\),
(25) applies throughout the annulus on its two-sheeted cover and
\[
                   |\widehat{\mathscr W}(z,\xi)|
                              \le C|\xi|^{-1/2}.
 \tag{28}
\]
The branch is reached from the canonical germ by a fixed path in
the scaled \(\eta\)-plane to the inner circle, followed by continuation
in (27). At a fixed nonzero \(\xi\), (8) extends holomorphically across
\(z=0\) after choosing a local square root of \(-\xi/\eta_*\).
This supplies an outer cutoff independent of \(z\); it is not an
infinite Laplace ray or a statement about a cutoff residual.

## 5. The exact second exceptional restriction and the classical action

Use the literal coefficient expansions of [J]:
\[
 a_{11}=Bz+b_{11}z^2+O(z^3),\quad
 a_{22}=A+b_{22}z+O(z^2),\quad a_{33}=a_{33}(0)+O(z).
 \tag{29}
\]
Put
\[
 \mathfrak d=b_{11}-\frac BA b_{22}
                          +\frac{B^2}{A^2}a_{33}(0).
 \tag{30}
\]
Let \(c_k=c_{kk}\), the coefficient of \(s^{-2k-1}\) in \(b_k\).
In the forcing of this pole, (13) requires \(p=k-1,\ell=n\).
Equation (11) then requires \(n+v=3\); the only possibilities are
\((n,\ell,v)=(1,1,2),(2,2,1),(3,3,0)\).
They are all principal-symbol terms.

For a leading input \(c_p s^m\), \(m=-2p-1\), the leading coefficient
of \(I^{n-1}P_n(p-2\theta)b_p\) is
\[
                   m(-B/A)^{n-1}c_p\,s^{m-2}.
 \tag{31}
\]
Indeed the successive derivative factors
\(m(m-2)\cdots(m-2n+2)\) cancel the denominators of the \(n-1\)
primitives. The minus sign defining \(F_k\) in [J] gives
\((2k-1)\mathfrak d\,c_{k-1}\).
On the other side, (18) gives the leading coefficient
\(-3Bk c_k\). Therefore
\[
 c_0=r,\qquad
 c_k=-\frac{\mathfrak d}{3B}\frac{2k-1}{k}c_{k-1},
 \qquad
 H(0,0,u)=r\left(1+\frac{2\mathfrak d}{3B}u\right)^{-1/2}.
 \tag{32}
\]
The last equality is a convergent germ, by (25). It includes the
case \(\mathfrak d=0\), when this restriction is constant.

Its coefficient agrees with the cubic term of the actual classical
action. To check this without a WKB premise, write
\[
 P(\alpha+z,1+v)
 =v\{p_1z+p_2z^2+q_0v+q_1zv+t_0v^2
                                  +O((z,v)^3)\}.
 \tag{33}
\]
Here \(B=\alpha p_1,\ A=\alpha^2q_0\). The nonabelian classical root
\(\ell(\alpha+z)=1+\ell_1z+\ell_2z^2+\cdots\) has
\[
 \ell_1=-p_1/q_0,\qquad
 \ell_2=-(p_2+q_1\ell_1+t_0\ell_1^2)/q_0.
 \tag{34}
\]
Define the local analytic action by
\(S(\alpha)=0,\ S'(Y)=\log\ell(Y)/Y\), with \(\log\ell(\alpha)=0\).
Then
\[
 -\frac{S(\alpha+z)}{z^2}=\eta_*+\sigma_1z+O(z^2),\qquad
 \sigma_1=-\frac{\ell_2}{3\alpha}
          +\frac{\ell_1^2}{6\alpha}+\frac{\ell_1}{3\alpha^2}.
 \tag{35}
\]
The actual finite-shift formula (8) of [J] gives
\[
 b_{11}=p_1+\alpha p_2,\quad
 b_{22}=2\alpha q_0+\alpha^2q_1+\tfrac12\alpha^2p_1,\quad
 a_{33}(0)=\alpha^3(t_0+q_0).
 \tag{36}
\]
Substitution in (30), using (34), yields
\[
                  \sigma_1=\frac{\mathfrak d}{3A},
 \qquad
 H(0,0,u)=r(1+\sigma_1u/\eta_*)^{-1/2}.
 \tag{37}
\]
Thus the second exceptional restriction has exactly the action-predicted
cubic displacement. This calculation does not establish that the full
singular set is the single curve \(\xi=-S(Y)\), or that (25) continues
through its displayed \(u\)-singularity with a specified local form.

## 6. Complete proof source and limits

The sole proof direct is:

| Label | Complete source | SHA256 |
|---|---|---|
| J | notes/research_classical_verma_borel_joint_continuation.md | 67cbb4c1577af04336b53985e867f6d2adc7e184c6d4276c53a0888f57d8ded8 |

J supplies the actual canonical meromorphic-loop germ, ordered
coefficient hierarchy, finite-shift expansion and initial joint
holomorphy. All Laurent closure, resonance resolution, coefficient
bounds, coordinate changes and action calculations are proved here.

The result concerns an actual operator node at a simple Alexander root.
It does not identify that component with the canonical hyperbolic
representation component. The broad arbitrary-short-filling target
also includes \(\Delta_K=1\), for which this pole seed is absent.
No full moving-singularity theorem, infinite-ray summation, original
cycle selection or volume lower bound is asserted.
Only written mathematics and source-text reads were used. Frozen
proofs and public manuscripts are unchanged.
