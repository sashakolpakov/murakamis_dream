# An exact Fourier replacement for the first type-three cap

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The physical first-cap reduction can be used in the whole original
Fourier contraction without substituting an arbitrary off-grid
interpolant. It introduces one explicit Fourier weight and its wrapped
term. The remaining cap factor is one fixed polynomial and has a genuine
complex packet on a neighborhood of the real outgoing interval. The
wrapped term is retained exactly; this note does not estimate the full
remaining outer integration cycle.

## 1. The polynomial remainder and its exact contraction

Retain \(P_j=(r;r)_j\), \(r=e^{-2\pi i/N}\),
\(p_l(X)=(rX;r)_l\), and the original Newton polynomials \(e_l(w)\).
Let \(d_N\) be the unique polynomial of degree less than \(N\)
with \(d_N(r^j)=1/P_j\). Define the fixed polynomial
\[
 \mathcal K_N(w,X)=\sum_{l=0}^{N-1}
       (-q)^{-l}e_l(w)\frac{p_l(X)}{P_l^2},\qquad q=e^{\pi i/N}.
 \tag{1}
\]
Write \(K_{k,N}=(-1)^k\partial_w^k\mathcal K_N|_{w=-2}\).
All these polynomials have degree less than \(N\).
The original cap polynomial \(\mathcal U_{0,N}\) is the one in
[the exact open-word source](research_mixed_conditional_torus_composition.md#5-open-words-with-the-original-complete-boundary-jets).

**Lemma 1.** The following is an identity of original polynomials,
not only of their asymptotic phases:
\[
 \mathcal U_{0,N}(w,X)
   =\operatorname{rem}_{X^N-1}\bigl[N d_N(X)\mathcal K_N(w,X)\bigr].
 \tag{2}
\]
If \(G(X)\) is any Laurent polynomial with band
\([-N+1,0]\), then for every positive circle radius,
\[
 \oint \mathcal U_{0,N}(w,X)G(X)\frac{dX}{2\pi iX}
   =N\oint \mathcal K_N(w,X)G(X)d_N(X)(1+X^{-N})
                                                   \frac{dX}{2\pi iX}.
 \tag{3}
\]
Both identities retain the entire ordinary boundary polynomial and
all its derivatives.

*Proof.* The exact terminating reduction of
[the physical cap theorem, Lemma 1](research_mixed_three_first_cap_packet.md#1-exact-reduction-of-the-original-source)
gives \(\mathcal U_{0,N}(w,r^j)=N\mathcal K_N(w,r^j)/P_j\).
Both sides of (2) have degree less than \(N\), and these are all
\(N\) distinct roots. Hence (2) follows. To verify (3) without
using a sampled Fourier rule, write
\(Nd_N\mathcal K_N=L+X^NH\), with \(\deg L<N\) and
\(\deg H\le N-2\). Its remainder is \(L+H\).
In the Laurent products, \(X^NHG\) has only strictly positive
powers and \(X^{-N}LG\) only strictly negative powers. The constant
coefficient of \((L+X^NH)(1+X^{-N})G\) is consequently precisely
the constant coefficient of \((L+H)G\). This proves (3) on every
radius. Differentiation in the ordinary color commutes with these
finite polynomial identities. \(\square\)

For an open word beginning with type three, every literal next kernel
\(C_{\epsilon,N}(X,Y)\), considered as a function of \(X\), has
band \([-N+1,0]\). For a one-vertex word, the remaining endpoint
\(H_{N,b}(X^{-1})\) has that same band. Thus (3) applies pointwise
in all other Fourier variables to the actual complete source.

More explicitly let \(m\ge1\), \(\epsilon_1=0\),
\(c_4=\sum_v\epsilon_v\), and
\(W_N(X)=d_N(X)(1+X^{-N})\). The complete ordinary jets obey
\[
 \begin{split}
 \mathcal Z_N^{a,b}
 ={}&(-1)^{a+b}\kappa^{m+c_4}N^{m+c_4+1}
 \oint\cdots\oint K_{a,N}(X_1)
       \prod_{v=2}^m C_{\epsilon_v,N}(X_{v-1},X_v)\\
 &\qquad\qquad\times H_{N,b}(X_m^{-1})\,
       W_N(X_1)\prod_{v=2}^m W_N(X_v)^{\epsilon_v}
                           \prod_{v=1}^m\frac{dX_v}{2\pi iX_v}.
 \end{split}                                                     \tag{4}
\]
This is the original exact source and original carrier, with the extra
factor \(N\) explicitly displayed. Empty products give the same
statement for \(m=1\). No knot identification is inferred from this
scalar formula. A whole-color version replaces the two jet endpoint
factors by their original polynomial versions and removes the sign.

## 2. A genuine packet for the fixed cap polynomial

Put \(X=e^{-2\pi iz}\), \(I=[1/5,9/20]\). Use \(T(z,u)\),
its original critical point \(u_*(z)\), and its absolute normalization
from [the physical cap theorem](research_mixed_three_first_cap_packet.md).
Set
\[
 \begin{split}
 \Theta(z,u)&=T(z,u)+g(z),\qquad
                     g(z)=J(z)+i\pi(z-z^2)/2,\\
 B_k(z)&=\frac{\sqrt{2\pi}}{\sqrt{-T_{uu}(z,u_*)}}
 e^{-i\pi u_*/2}
 \frac{\sqrt{2\sin\pi(u_*+z)}}
      {\sqrt{2\sin\pi z}(2\sin\pi u_*)^2}
 \left(\frac{\tan\pi u_*}{4\pi}\right)^k.
 \end{split}                                                     \tag{5}
\]
All branches are those fixed in the physical theorem.

**Theorem 2.** There is a fixed complex neighborhood of \(I\)
on which the literal fixed polynomial (1) satisfies
\[
 K_{k,N}(e^{-2\pi iz})
   =N^{k-3/2} B_k(z)e^{N\Theta(z,u_*(z))}
                                      \{1+O_k(N^{-1})\}.        \tag{6}
\]
The coefficient is holomorphic and nonzero. The normalized error is
holomorphic, uniformly with every fixed outgoing derivative on smaller
neighborhoods. There is also a joint neighborhood of
\(I\times\{-2\}\) in \((z,w)\) on which
\[
 \mathcal K_N(w,e^{-2\pi iz})
   =N^{-3/2}\mathcal B(z,w)e^{N\mathcal S(z,w)}
                                      \{1+O(N^{-1})\},          \tag{7}
\]
with nonzero holomorphic coefficient and all fixed joint derivatives.
Both level parities are included. No quantified distant cyclic image
is asserted to lie in this neighborhood.

*Proof.* On the retained rectangle
\([.1,.4]+i[-.12,.12]\), the exact identity
\[
 p_l(e^{-2\pi iz})
       =\widehat P_N(Nz+l)/\widehat P_N(Nz)
 \tag{8}
\]
gives one holomorphic index interpolation, where \(\widehat P_N\)
is the prescribed marked sine factorial. It is nonzero on a
neighborhood of this entire rectangle for \(z\) near \(I\).
The middle summand of (1) has power \(N^{k-2}\), phase \(\Theta\),
and amplitude
\[
 e^{-i\pi u/2}
 \frac{\sqrt{2\sin\pi(u+z)}}
      {\sqrt{2\sin\pi z}(2\sin\pi u)^2}
 \left(\frac{\tan\pi u}{4\pi}\right)^k.
 \tag{9}
\]
Thus the full contour calculation in the physical theorem applies
verbatim to these retained rows: adding \(g(z)\) changes none of the
index derivatives or relative side and alias gaps. It gives the
coefficient (5), including the power
\(N^{k-2}\cdot N\cdot N^{-1/2}=N^{k-3/2}\).

It remains to justify every row of the fixed polynomial, including the
rows that vanished on the physical grid. For real \(z\in I\), their
upper entropy is
\[
 Q_K(z,u)=\mathcal V(u)+J_{\rm per}(u+z)-J(z)-2J(u),
                                      \qquad0\le u\le1.        \tag{10}
\]
Here \(J_{\rm per}\) is the periodic real primitive of
\(\log(2|\sin\pi v|)\), agreeing with \(J\) on \([0,1]\).
Below \(u=1-z\), this is the entropy in the physical theorem
plus \(J(z)\); all its real tails therefore already have a uniform
strict gap. If \(u\ge1-z\), then \(u\ge11/20\), so
\(\mathcal V(u)\le0\) and \(J(u)\ge0\). Also
\(u+z-1\in[0,z]\subset[0,9/20]\), where \(J\le0\). Consequently
\[
 Q_K(z,u)\le-J(z)<1/6,
 \qquad
 \Re\Theta(z,u_*)>26/25-1/6=131/150.                          \tag{11}
\]
The extra full-index rows have a particularly large reserve.

For small complex perturbations of \(z\), estimate each exact product
factor by
\[
 |1-e^{-2\pi i(z+h/N)}|
 \le |1-e^{-2\pi i(z_0+h/N)}|+C|z-z_0|,
                                      \quad z_0\in I.
\]
The regularized logarithmic Riemann sum differs from its real primitive
by at most \(CN\delta(1+|\log\delta|)+O_\delta(1)\), uniformly in
its upper row and through its zeros. This is precisely the elementary
finite-product regularization proved in
[the canonical type-four continuation, Lemma 2](research_mixed_four_conditional_complex_neighbors.md).
For the whole ordinary boundary polynomial, the independent Newton
product estimate adds \(CN\sqrt{|w+2|}\), as proved in
[the full-index boundary theorem, Section 7](research_complete_boundary_full_index_interval.md#7-the-whole-boundary-polynomial-near-the-complete-color).
Neither estimate divides by a physical zero. The strict real tail
gaps, including (11), therefore persist on a fixed joint neighborhood.

All central contour factors remain regular there. Their side and
cotangent gaps persist by continuity, and the simple root continues.
The exact two factorials at the complete end give the phase
\(\Theta\) with \(V_0(u)\) replaced by
\(-J(.5-u+t/(2\pi))-J(.5-u-t/(2\pi))-2J(u)\),
where \(w=-2\cos t\). The amplitude (9) for \(k=0\) is unchanged.
Evenness in \(t\), uniqueness, and \(w+2=t^2+O(t^4)\) give the
ordinary-color holomorphic phase and coefficient in (7). Cauchy's
formula proves the uniform derivative assertions and recovers (6).
This establishes a packet for the single actual polynomial (1), not
for an unspecified interpolation of its physical values. \(\square\)

## 3. What remains in the full mixed component

Equation (4) absorbs the polynomial remainder into a complete original
Fourier contraction. It retains \(d_N(X_1)X_1^{-N}\) explicitly;
no smallness of that term follows from (6). The new factor has a
packet near the real outgoing arc, but using it at a particular complex
outer critical point requires a quantified continuation or a separate
full source contour. The remaining global outer complements and the
new first-variable alias still require estimates. Thus this is an
exact boundary-source replacement with a genuine local packet, not a
full mixed-word volume theorem.

## 4. Reproduction

```sh
python3 experiments/check_mixed_three_first_cap_fourier_reduction.py
```

The checker uses exact algebraic-number arithmetic for the original
polynomials, the remainder and every negative Fourier monomial at
levels two, three, four and six, with ordinary orders zero through two.
The all-level proof is Lemma 1; these finite calculations test its
source and carrier normalization. It also verifies the current
physical-packet record and the exact amplitude/degree relation used
in (5)--(9).
