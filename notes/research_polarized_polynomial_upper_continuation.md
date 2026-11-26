# Polynomial upper bounds for an initialized polarized source

Private written proof, 22 November 2026.

An action-relative complex upper bound may lose any fixed power of the
level. An actual all-order initializer still propagates through that loss,
provided its formal coefficients extend holomorphically. A finite jet of
those coefficients suffices for a nonzero leading term at a fixed target.
This is a source-specific use of elementary analytic continuation, not a
new estimate for the original period.

## 1. Polynomial losses and a holomorphic initializer

Let \(D\subset\mathbb C\) be connected and open, and let
\(U\subset D\) be a nonempty open set. Suppose \(f_N\) is holomorphic
on \(D\), with \(N\) tending to infinity through an unbounded subset of
the positive integers. Assume:

1. For every compact \(K\Subset D\), there are constants \(C_K,B_K\)
   such that
   \[
                         \sup_K|f_N|\le C_KN^{B_K}.
   \tag{1}
   \]
2. There are holomorphic functions \(a_j\) on \(D\), \(j\ge0\), and
   for every integer \(L\ge1\),
   \[
   f_N-\sum_{j=0}^{L-1}a_jN^{-j}=O_{\mathrm{loc},U}(N^{-L}).
   \tag{2}
   \]

Then (2) holds locally uniformly on all of \(D\), at every order.
It also holds after any fixed number of complex derivatives.

Here and below all constants may depend on the chosen order. The
polynomial exponent used to propagate a remainder will not depend on
that order.

**Proof.** Fix a compact target set \(K\Subset D\). Choose a closed
disk in \(U\), finitely many paths in \(D\) joining that disk to a
finite disk cover of \(K\), and a compact neighborhood of these paths.
There is a common \(r>0\) and a finite collection of disk chains with
successive centers at distance at most \(r\), whose disks of radius
\(4r\) remain in that compact neighborhood. Their final disks of radius
\(2r\) cover \(K\); the initial disk of radius \(r\) lies in \(U\).
Let \(J\ge1\) bound the number of interpolation steps in every chain.

For
\[
                 R_{L,N}=f_N-\sum_{j=0}^{L-1}a_jN^{-j},
\]
(1) and boundedness of the finitely many \(a_j\) on this fixed compact
neighborhood give
\[
                  |R_{L,N}|\le C_LN^B,\qquad B\ge0,
   \tag{3}
\]
where \(B\) is independent of \(L\). The initial disk has bound
\(O_L(N^{-L})\).

For a holomorphic function with inner bound \(M_1\) on radius \(r\)
and outer bound \(M_4\) on radius \(4r\), the maximum principle gives
the radius-\(2r\) bound
\[
                             M_2\le M_1^{1/2}M_4^{1/2}.
   \tag{4}
\]
Indeed compare \(\log|R|\) on the intervening annulus with the harmonic
function affine in \(\log|z-z_0|\) with those two boundary values.
Zeros are handled by the usual subharmonic inequality, or by a
positive regularization of the boundary bounds.

The next radius-\(r\) disk lies in the preceding radius-\(2r\) disk.
Iterating (4), and using (3) at every outer disk, therefore gives
\[
 \sup_K|R_{L,N}|
       \le C_{K,L}N^{-L\theta+B(1-\theta)},\qquad
                         \theta=2^{-J}>0.
   \tag{5}
\]
Shorter chains obey the same weaker bound. The fixed finite cover makes
\(J,B\) common to all of \(K\), independently of \(L\).

For any desired order \(M\ge1\), choose \(L\ge M\) so that
\(L\theta-B(1-\theta)\ge M\). Equation (5), followed by adding back
the finite tail \(\sum_{j=M}^{L-1}a_jN^{-j}=O_K(N^{-M})\), proves
the order-\(M\) assertion. Apply it on a slightly larger compact set
and use the Cauchy integral formula to obtain derivatives. \(\square\)

There is a useful finite version. If only \(a_0,\ldots,a_{L-1}\)
extend to \(D\), and only their order-\(L\) seed estimate is supplied,
the same proof gives order \(M\) wherever
\[
              L\ge M,\qquad L\theta-B(1-\theta)\ge M.
   \tag{6}
\]
In particular a fixed integer
\[
                  L\ge \max\{1,\,2^J(B+1)-B\}
   \tag{7}
\]
suffices for \(f_N=a_0+O_K(N^{-1})\). This jet length depends on the
domain, upper-bound exponent and disk chains, but not on \(N\).
Nonvanishing at a target still requires \(a_0\) to be nonzero there.

The upper hypothesis may instead be the local complex-area estimate
\[
                \int_K|f_N(z)|^2\,dA(z)\le C_KN^{2B_K}
                \quad(K\Subset D).
   \tag{8}
\]
To recover (1), first enlarge \(K\) inside \(D\), then apply the
holomorphic submean inequality on disks of a fixed buffered radius.
This uses area on complex disks, not a bound only on their real axes.

## 2. The actual initialized contour representative

Fix the finite same-index graph and selected vertices of the
pattern-adapted source theorem. Write \(m=|I|\), let \(e\) be its number
of incident kernel edges counted once, and keep outside angles equal
to zero, hence outside spectral values equal to \(-2\). Fix real
powers \(\mathbf b\) before taking \(N\to\infty\). Integral powers give
the prescribed physical crossings.

Choose one small positive diagonal base charge and freeze the entire
table of heights, cuts and oriented currents prescribed in that theorem.
For one complex charge set
\[
 \mathscr G_N(\chi)
     =\mathfrak Z_{N,\mathbf+}(\mathbf b,\chi\mathbf1;\mathbf0),
 \qquad \beta=\frac{3(m-e)}2,\qquad
 \varepsilon_N=\prod_{v\in I}
                     e^{\pi i b_v(N-1)^2/(4N)}.
   \tag{9}
\]
The source theorem gives an entire function of \(\chi\). On a genuine
fixed complex seed neighborhood it gives an expansion to every fixed
order, whose leading coefficient is \(2^mA_\Gamma\ne0\).
The heights are not reselected as \(\chi\) changes.

Let \(D\) be a connected charge domain containing that seed and the
target \(1\). Suppose \(S\) is holomorphic on \(D\) and restricts to
the initialized marked action. Define
\[
                         f_N(\chi)=N^{-\beta}e^{-NS(\chi)}
                                                   \mathscr G_N(\chi).
   \tag{10}
\]
If its initialized formal coefficients extend holomorphically to \(D\)
and it has the local polynomial bounds (1) or (8), Section 1 propagates
its full expansion. For a leading result only the finite jet (6)--(7)
is needed. If its continued leading coefficient satisfies \(a_0(1)\ne0\),
the exact endpoint identity gives
\[
 Z_N^{\mathrm{original}}
   =\varepsilon_N\mathscr G_N(1)
   =\varepsilon_NN^\beta e^{NS(1)}
                         \{a_0(1)+O(N^{-1})\}.
   \tag{11}
\]
Here \(Z_N^{\mathrm{original}}\) is the original marked source in the
pinned contour construction, with its full phases and normal data.
Since the fixed powers are real, \(|\varepsilon_N|=1\).

One may apply the analytic theorem separately to even and odd levels
if their formal coefficients differ. The full-sequence leading rate
then follows when both target leading coefficients are nonzero and
the same marked action is used. A fixed, \(N\)-independent holomorphic
charge curve through the seed and the target may replace the diagonal.
Its image must retain the asserted initializer and action charts.

This application holds the outside data at their complete values.
The exact identities allow ordinary free outside variables, but the
quoted initializer does not establish an open seed in those variables.
No such boundary initializer is inferred here.

The heat-readout quotient theorem permits the initialized representative
in (9) in place of the canonical spectral polarization: their difference
has exactly zero readout after every independent signed heat evolution.
It does not supply (1), (8), formal-coefficient continuation or a target
unit. In particular the cosine family and the canonical finite coupon
cannot be substituted for \(\mathscr G_N\) away from unit charge.

## 3. A source-faithful quadratic upper trial

There is a direct positive upper trial for this off-endpoint source,
without claiming that an existing physical-algebra quartic compiles it.
Keep its actual ordinary polynomial numerator \(F_N(\mathbf z)\)
unreduced. For the same-index kernel product,
\[
 \deg_{z_v}F_N\le D_v=d_v(N-1),\qquad
 f_N^{\mathrm{coef}}\in
             \bigotimes_{v\in I}\mathbb C^{D_v+1}.
   \tag{12}
\]
Here \(d_v\) counts original incidences, including two for a loop;
the crossing Gaussians belong to the trace rows, not this numerator.
The coefficient-space dimension is \(O_\Gamma(N^m)\).

Define a row \(\ell_N(\chi)\) by applying the exact frozen operator
in the pattern-adapted formula to each ordinary monomial:
\[
 \ell_N(\chi)=
 \sum_{S\subseteq I}\bigotimes_{v\in I}
 \begin{cases}
   \mathcal O_{v,b_v,\chi},&v\in S,\\
   \mathcal H_{+,b_v,\chi}^{h_v^S}
            +\mathcal V_{b_v,\chi}^{h_v^S,\epsilon_v},&v\notin S.
 \end{cases}
 \qquad
                  \mathscr G_N(\chi)=\ell_N(\chi)f_N^{\mathrm{coef}}.
   \tag{13}
\]
The tensor rows in (13) act on the monomial basis of (12).
Their entries are the prescribed local physical-row sums, with their
first normals, and fixed compact contour integrals. There is no
reduction modulo \(P_N\) in (12)--(13). Such a reduction is generally
invalid for this representative away from the endpoint.

In the ordinary coefficient Euclidean metric put
\[
 r_N=\|\ell_N(\chi)\|^2,\quad \lambda_N=1+r_N,\qquad
 J_{N,\chi}(x)=\lambda_N\|x-f_N^{\mathrm{coef}}\|^2
                                      +|\ell_N(\chi)x|^2.
   \tag{14}
\]
Completion of the rank-one square gives, with \(G=\ell_Nf_N^{\mathrm{coef}}\),
\[
 x_* =f_N^{\mathrm{coef}}-\frac{\ell_N^*G}{\lambda_N+r_N},
 \qquad
 \min J_{N,\chi}=\frac{|G|^2}{1+r_N/\lambda_N},
 \qquad
                         |\mathscr G_N(\chi)|^2\le2J_{N,\chi}(x).
   \tag{15}
\]
The coefficient matrix is \(\lambda_NI+\ell_N^*\ell_N\), with
condition number at most \((\lambda_N+r_N)/\lambda_N<2\).
This is a generic least-squares calculation, not a new growth bound.
The data \(f_N^{\mathrm{coef}},\ell_N\) are specified without inserting
or dividing by the unknown closed source; their construction and the
choice of a useful trial may nevertheless be costly.

Consequently any supplied trials \(x_N(\chi)\) satisfying
\[
 \int_K 2N^{-2\beta}e^{-2N\Re S(\chi)}
                 J_{N,\chi}(x_N(\chi))\,dA(\chi)
                          \le C_KN^{2B_K}\quad(K\Subset D)
   \tag{16}
\]
supply (8). The trials and \(\lambda_N\) need not be holomorphic;
the actual source (10) is holomorphic. No estimate (16) is proved here.

## 4. What has been reduced

The continuation criterion asks only for an action-relative complex
UPPER estimate with an arbitrary fixed polynomial loss. It does not
ask for a residual lower witness or exact asymptotic power in that
upper estimate. The cost of the loss is a finite number of continued
formal coefficients when only the leading term is wanted.

The remaining inputs are substantial: a connected regular action
domain to the actual target, the required formal jet on that domain,
a nonzero target density, and the complex upper estimate itself.
A real-charge upper estimate is insufficient for the proof. A zero
of the continued leading coefficient does not yield (11) with a
nonzero leading term. Exact source-null freedom alone proves none of
these analytic inputs.

For a knot-volume conclusion one must additionally retain the exact
source-to-knot normalization and peripheral marking, and establish
\(2\pi\Re S(1)=\operatorname{Vol}\). Known unit or polynomial factors
do not change that rate; omitted source factors are not licensed.
No new filling class or volume lower bound is established here.

## Direct sources and versions

Both complete direct sources and the complete final proof are read
before freezing. The continuation proof above imports no source
asymptotic beyond the initializer explicitly stated in Section 2.

- [Pattern-adapted initialized family](research_pattern_adapted_polarized_heat_initializer.md),
  a27c25dae7f3be3f1ef52fb369ecca822b0896a4b034450131e05b12423c2694:
  exact frozen polynomial source, all-order complex initializer,
  original carriers, full normals and literal endpoint identity.
- [Exact heat-readout quotient](research_polarized_endpoint_heat_readout_quotient.md),
  32acb79c4f1fff481671d8205454a91b6a1eaf5704b6582b2affb901270e8ede:
  comparison with the canonical polarization in the precise readout
  kernel, retaining complete heat currents rather than a saddle piece.
