# An exact auxiliary-height identity for the original marked closing

24 November 2026. Written research proof.

For every actual signed word, the original cup and last marked closing
give a one-dimensional family over the bottom auxiliary coideal heights.
Its known height dependence has degree determined only by the width.
The proof keeps the full nested frame and computes the marked seam
at every auxiliary height, including its phase. The resulting positive
Fourier energy is exactly the original squared scalar times a known factor.
It does not estimate that scalar or identify an auxiliary height with
a knot meridian.

## 1. Full nested frames at every bottom parameter

Use the complete physical conventions of H and T:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1}=q^d,\quad \sqrt q=e^{\pi i/(2N)},\quad
 F_a=(Q;Q)_a,\quad F_0=1,\quad F_d=N.
\]
Here \((z;Q)_a=\prod_{h=0}^{a-1}(1-zQ^h)\), with empty product one.
The physical one-head basis \(e_a\), \(0\le a\le d\), is orthonormal, and
\[
 Ke_a=xQ^{-a}e_a,\quad Ee_a=(Q^{-a}-1)e_{a-1},\quad
 Fe_a=(1-Q^{a+1})e_{a+1}.
\]
Missing endpoint arrows are zero. Use the ordered coproducts
\(K_{12}=K_1K_2\), \(E_{12}=E_1K_2+E_2\),
\(F_{12}=F_1+K_1^{-1}F_2\), iterated in the physical head order.
The roots and monic polynomial are
\[
 \mu_l=Q^l+qQ^{-l}\quad(0\le l<N),\qquad
 \lambda_r=2\sqrt q\cos\alpha_r,\quad
 \alpha_r=(r+\tfrac12)\pi/N,\quad
 p_N(z)=2q^{N/2}T_N(z/(2\sqrt q)).
 \tag{1}
\]
Here \(T_N\) is Chebyshev of the first kind. The two root lists
are permutations of each other.
For an actual root \(\sigma\), write
\[
 u_\lambda(\sigma)_a=q^{-a}D_a(\lambda;\sigma)/F_a,
\]
\[
 D_{-1}=0,\quad D_0=1,\qquad
 D_{a+1}(\lambda;\sigma)
   =(\lambda+qQ^a\sigma)D_a-q(1-Q^a)^2D_{a-1}.
 \tag{2}
\]
Every first component of \(u_\lambda(\sigma)\) is one.

On \(r\) heads let
\[
 B_\sigma^{(r)}
   =\mathsf F-(\mathsf E-\sigma I)\mathsf K^{-1},
 \qquad B_\sigma^{(0)}=\sigma.
\]
T's continuant identity, or induction on the first-head block, gives
\(p_N(B_\sigma^{(r)})=0\). At each tail eigenvalue, the one-head
eigenmatrix with columns (2) is invertible: it is a triangular
coefficient matrix with nonzero diagonal times a Vandermonde.
Thus tail-up reconstruction gives a full basis, with no quotient.

More explicitly, at width \(b\), set \(\nu_b=\sigma\) and let
\(\nu_0,\ldots,\nu_{b-1}\) range independently over all \(N\) roots.
The columns of the full \(N^b\)-dimensional frame are
\[
 \Psi_\sigma(\boldsymbol\nu)
       =\bigotimes_{j=1}^b u_{\nu_{j-1}}(\nu_j).
 \tag{3}
\]
This is H(12) with its bottom parameter left variable.
Induction using the invertible one-head matrices proves that
\(\Psi_\sigma\) is invertible. The external label \(\nu_0=\eta\)
is precisely the eigenspace \(B_\sigma^{(b)}=\eta I\).

The positive height metric used below is also specified explicitly.
Put \(\theta=\pi/(2N)\), and let \(\alpha_\nu\) be the sorted angle of \(\nu\).
Use \(H_N'e_a=q^{1+d/2+a}e_{d-a}\). H's one-head signed
orthogonality is independent of the tail root.
Writing \(\nu_j=\lambda_{r_j}\), it gives, by the deepest differing
path label,
\[
 \Psi_\sigma^\dagger(H_N')^{\otimes b}\Psi_\sigma
      =\operatorname{diag}\prod_{j=0}^{b-1}
                    (-1)^{r_j+1}\csc\alpha_{r_j}.
\]
Take the absolute value of this coordinate diagonal:
\[
 \mathcal D_{\boldsymbol\nu}
       =\prod_{j=0}^{b-1}\csc\alpha_{\nu_j},\qquad
 G_{{\rm ht},\sigma}
       =\Psi_\sigma^{-\dagger}\mathcal D\Psi_\sigma^{-1}.
 \tag{4}
\]
It is a positive physical-space form for this specified frame.
It is not \(\Psi_\sigma^\dagger\Psi_\sigma\), nor a common positive
metric in which all physical braids are unitary.

## 2. The marked diagonal seam is independent of the bottom height

Retain H's original ordinary cup \(\mathbf p\), ordinary cap \(\ell\),
and marked cap \(m\). In the physical basis their literal coefficients are
\[
 (\mathbf p)_{ab}=Nx^{-b}\mathbf1_{a+b=d},\quad
 \ell_{ab}=\frac{x^a}{N}\mathbf1_{a+b=d},\quad
 m_{ab}=\frac{x^b}{N^2}.
\]
The marked row has no degree delta. Define
\[
 A_\lambda=\frac{N^2q^dx^{-d}}{p_N'(\lambda)},\qquad
 \mu_*=-q^{-1}-q^2=\lambda_{N-2},\qquad
 T_*=\frac{2}{N(1-q^{-3})}.
\]
H already proves, at every tail root \(\sigma\),
\[
 \mathbf p\otimes z_\sigma
   =\sum_\lambda A_\lambda\,
      u_\sigma(\lambda)\otimes u_\lambda(\sigma)\otimes z_\sigma,
\]
\[
 \ell[u_\eta(\lambda)\otimes u_\lambda(\sigma)]
           =\delta_{\eta,\sigma}/A_\sigma .
 \tag{5}
\]
The unrestricted marked tensor remains
\[
 m[u_\eta(\lambda)\otimes u_\lambda(\sigma)]
   =\frac1{N^2}\Phi_{\eta,\lambda}(q^{-1})
                         \Phi_{\lambda,\sigma}(-q^{-2}),\qquad
 \Phi_{\lambda,\sigma}(z)=\sum_{a=0}^dD_a(\lambda;\sigma)z^a/F_a.
 \tag{6}
\]
The new exact diagonal evaluation is
\[
 \boxed{\quad
 m[u_\sigma(\lambda)\otimes u_\lambda(\sigma)]
                 =\delta_{\lambda,\mu_*}T_*
 \quad\hbox{for every actual root }\sigma .
 \quad}                                                       \tag{7}
\]
No assertion replacing (6) is made when \(\eta\ne\sigma\).

Here is a finite proof with its source phase. Use cyclic labels
\(\lambda=\mu_j,\sigma=\mu_l\), \(m_0=\lfloor N/2\rfloor\), and set
\[
 a=\begin{cases}[m_0-j-l]_N,&N\ {\rm even},\\
                 [m_0+j-l]_N,&N\ {\rm odd},\end{cases}
 \qquad 0\le a<N,\qquad b_0=d-a.
\]
T(16) gives the complete product
\[
 \Phi_{\mu_j,\mu_l}(z)
          =(-qQ^lz;Q)_a(-q^2Q^{-l}z;Q)_{b_0}.                 \tag{8}
\]
Reciprocity turns the diagonal value in (6) into
\(N^{-2}\overline{\Phi_{\lambda,\sigma}(-q)}
                         \Phi_{\lambda,\sigma}(-q^{-2})\).
At these two points the products in (8) are
\[
 (Q^{l+1};Q)_a(q^3Q^{-l};Q)_{b_0},\qquad
 (q^{-1}Q^l;Q)_a(Q^{-l};Q)_{b_0}.
\]
Odd powers of \(q\) cannot equal one. The first value is nonzero
exactly when \(a\le d-l\); the second exactly when \(a\ge d-l\).
Their product is therefore supported exactly at \(a=d-l,b_0=l\).
The formula for \(a\) gives \(j=[m_0+1]_N\) for even \(N\),
or \(j=m_0\) for odd \(N\). In both cases \(\mu_j=\mu_*\).

At this surviving index the two values are
\[
 \Phi(-q)=\frac{N}{F_l}(q^3Q^{-l};Q)_l,\qquad
 \Phi(-q^{-2})=(q^{-1}Q^l;Q)_{d-l}\,\overline{F_l}.
\]
Conjugation reverses the first odd string to \((q^{-1};Q)_l\).
Thus their conjugate product divided by \(N^2\) is
\[
 \frac1N(q^{-1};Q)_d=\frac{2}{N(1-q^{-3})}=T_* .              \tag{9}
\]
The last equality appends the one missing factor to the full
length-\(N\) product, whose value is \(1-q^{-N}=2\).
This proves (7), including \(l=0,d\), empty products, \(N=2\)
and composite levels. No absolute value replaced its phase.

## 3. The original source and closing in these frames

Now take even width \(b=2k\), \(k\ge1\), and let
\[
 u_0=\mathbf p^{\otimes k},\qquad
 \ell_0=\ell^{\otimes(k-1)}\otimes m,\qquad
 Z_N(R)=\ell_0 R u_0 .
\]
Here \(R\) is any actual unmarked signed braid word in the original
physical representation. The original scalar is
\(K_N=\chi_N Z_N(R)\);
no division by \(\chi_N\) or by \(Z_N(R)\) is used.

Write \(c=1+q\). The physical relations in H,T give
\(\mathsf K u_0=u_0\), \(B_c^{(b)}u_0=cu_0\),
\([R,\mathsf K]=0\) and \([R,B_c^{(b)}]=0\).
The first commutator also follows from preservation of integer degree.
Since
\[
 B_\sigma^{(b)}
   =B_c^{(b)}+(\sigma-c)\mathsf K^{-1},
\]
we obtain
\[
 B_\sigma^{(b)}u_0=\sigma u_0,\qquad
 [R,B_\sigma^{(b)}]=0 .                                    \tag{10}
\]
Construct the full frame (3) first, then restrict to its external
block \(\nu_0=\sigma\). Let \(\mathcal R_\sigma\) be the matrix of
\(R\) on that block, explicitly
\(\mathcal R_\sigma=(\Psi_\sigma^{-1}R\Psi_\sigma)|_{\nu_0=\sigma}\).
This preserves the original source exactly.
It does not identify the entire block with the saturated source.

For paths \((\nu_1,\ldots,\nu_{2k-1})\) in that block, define the
explicit column and row
\[
 a_\sigma(\boldsymbol\nu)
 =\prod_{i=1}^k A_{\nu_{2i-1}}
                  \prod_{i=1}^{k-1}\delta_{\nu_{2i},\sigma},
\]
\[
 b_\sigma(\boldsymbol\nu)
 =\delta_{\nu_{2k-1},\mu_*}
                  \prod_{i=1}^{k-1}\delta_{\nu_{2i},\sigma}.
 \tag{11}
\]
The symbol \(b_\sigma\) denotes an ordinary linear row, not a
Hermitian adjoint. Repeated use of the actual cup and ordinary cap
in (5), followed
by the marked evaluation (7), proves
\[
 u_0=\Psi_\sigma a_\sigma,\qquad
 \ell_0\Psi_\sigma\big|_{\nu_0=\sigma}
               =T_*A_\sigma^{-(k-1)}b_\sigma .
 \tag{12}
\]
In (12) the column is extended by zero outside its external block.
All internal labels not explicitly fixed in (11) remain summed.
No projection is inserted at an intermediate face.
In particular \(A_{\mu_*}T_*=1\), by T's derivative formula
or by the original cup and marked-cap normalization.

These exact arrays have polynomial boundary norms.
Set \(a=\sin\alpha_\sigma\), \(s_*=\sin(3\theta)\). The finite identity
\(\sum_{r=0}^d\sin\alpha_r=\csc\theta\), together with
\(|A_{\lambda_r}|=N\sin\alpha_r\), gives
\[
 \|u_0\|_{G_{{\rm ht},\sigma}}^2
               =[N^2\csc\theta/a]^k,
\]
\[
 \|\ell_0|_{\nu_0=\sigma}\|_{G_{{\rm ht},\sigma}^{-1}}^2
       =N^{-2k}a^{2-k}\frac{\csc^{k-1}\theta}{s_*}.
 \tag{13}
\]
For the second formula, inverse path weights contribute
\(a^k s_*\) and one sine sum for each of the \(k-1\) free odd labels;
the scalar is \(|T_*A_\sigma^{-(k-1)}|^2\).
The source and row norm product is polynomial in \(N\), uniformly
over all \(\sigma\), for each fixed width. This does not make
their angle after \(R\) positive or make \(R\) an isometry.

## 4. A whole-word auxiliary-height connection

Define the actual coherent contraction
\[
 \mathcal S_l(R)=b_{\mu_l}\mathcal R_{\mu_l}a_{\mu_l},
 \quad w_l=Q^l-qQ^{-l},\quad p=k-1,\quad
 \gamma_N=\frac N2q^dx^{-d}.
\]
Every word coefficient and every internal height sum is still inside
\(\mathcal S_l\). T's derivative formula gives
\[
 p_N'(\mu_l)=2N/w_l,\qquad A_{\mu_l}=\gamma_N w_l.
\]
None of the \(w_l\) vanishes: \(Q^{2l}=q\) would equate an even
power of \(q\) with an odd one. Equations (10)--(12) give the
whole-word identity
\[
 \boxed{\quad
 \mathcal S_l(R)=\frac{\gamma_N^p}{T_*}Z_N(R)\,w_l^p .
 \quad}                                                       \tag{14}
\]
Consequently, for all cyclic \(l\) modulo \(N\),
\[
 w_l^p\mathcal S_{l+1}(R)
             =w_{l+1}^p\mathcal S_l(R).                       \tag{15}
\]
The solution space of (15) is one-dimensional, pointed by \(w_l^p\).
Its unknown line coefficient is the original scalar in (14).
This is a line of closed contractions, not a rank-one physical source:
the full frame still has dimension \(N^b\).
The identity is valid for every signed word, irrespective of length;
its degree \(p\) depends only on width, not on filling twists.

The bottom auxiliary \(\sigma\) here replaces the constant \(c\)
in the nested coideal construction, with external height also \(\sigma\).
It is not an independently varied internal height, a physical color,
or a knot peripheral eigenvalue. The connection (15) depends on
\(N\) and width but not on \(R\); it is not a peripheral A-polynomial.
Formula (14) is not an off-root
continuation of a moving-color scalar. The Laurent representative
\((u-q/u)^p\) describes the root-grid values only. Substituting an
off-grid \(\sigma=u+q/u\) changes the finite tail spectral identities
and is not licensed by this theorem.

## 5. Exact Fourier support and positive energy

Use the normalized discrete transform
\[
 \widehat{\mathcal S}(n)
       =\frac1N\sum_{l=0}^{N-1}Q^{-nl}\mathcal S_l,\qquad
 c_N=\gamma_N^p Z_N(R)/T_*.
\]
For every \(N\), let
\[
 b_n=\sum_{\substack{0\le j\le p\\p-2j\equiv n\ ({\rm mod}\ N)}}
                    \binom pj(-q)^j,\qquad 0\le n<N.
\]
Expanding \(w_l^p\) in (14) proves
\[
 \widehat{\mathcal S}(n)=c_N b_n,\qquad
 M_{N,p}:=\sum_{n=0}^{N-1}|b_n|^2
            =\frac1N\sum_{l=0}^{N-1}|w_l|^{2p}>0 .
 \tag{16}
\]
This retains all aliases at small levels.
For \(N>2p\), the exponents \(p-2j\) are distinct modulo \(N\), so
\[
 M_{N,p}=\sum_{j=0}^p\binom pj^2=\binom{2p}p=:M_p.
 \tag{17}
\]
The last equality is the coefficient of \(t^p\) in
\((1+t)^p(1+t)^p\). In this range \(c_N=\widehat{\mathcal S}(p)\).

Parseval now gives the exact positive identity
\[
 \boxed{\quad
 |Z_N(R)|^2
   =|T_*|^2(2/N)^{2p}
       \frac{\sum_{l=0}^{N-1}|\mathcal S_l(R)|^2}{N M_{N,p}} .
 \quad}                                                       \tag{18}
\]
For \(N>2p\), replace \(M_{N,p}\) by the fixed integer \(M_p\).
The corresponding original squared scalar is \(|\chi_N|^2\)
times (18). The coherent word sums remain inside each absolute
square; no absolute-value substitution was made within a word.

When \(N>2p\) and \(Z_N(R)\ne0\), the angle between the vector
\((\mathcal S_l)\) and the highest Fourier character \((Q^{pl})\)
has absolute cosine \(M_p^{-1/2}\).
This is an auxiliary-index observation angle, not a lower bound
for the physical marked angle of the full propagated state.
If \(Z_N(R)=0\), the section and the energy both vanish, and all
identities above remain valid without division by the scalar.

## 6. Coverage and remaining scope

H already gives the nested frame at bottom \(c\), general ordinary
boundary tensors, and the marked tensor (6), with its diagonal
evaluation at \(c\). T gives the all-root finite product (8),
the full graph construction and the actual commuting word action.
The new steps are the diagonal marked seam at every bottom root,
the explicit full-width boundary arrays, and the resulting initialized
whole-word auxiliary-height line and Fourier energy.

The separate initialized-period and bidiagonal-transport notes
concern a fixed local source and neighboring-frame comparisons.
Their norm estimates are not substituted for (14)'s full word.
The simple coideal frame is not identified as an algebra with the
confluent pair-Casimir compiler; its full Hermite and source constraints
are retained by the original physical maps.

The Fourier energy is an exact representation, not a geometric
evaluation. It neither proves this energy strictly positive for every knot
nor compares its growth with hyperbolic volume. No original phase,
last marked cap, shared height, external scalar, or normal direction
has been removed. The arbitrary-short-filling finite-exception
target remains open.

| Complete input | Lines | SHA256 |
| --- | ---: | --- |
| [Height pairing and marked boundary](research_coideal_height_pairing_and_marked_boundary.md) | 543 | bed81fcb12b20d16d41c55b476b13d8d69b1fe79d0d0620c31230ba652b1d82f |
| [Exact crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
