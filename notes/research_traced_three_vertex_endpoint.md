# The endpoint contribution to a traced three-crossing vertex

Research note, 3 November 2026.

Restoring the vertex traces gives an exact Fourier representation of a
circle-tree source. It is therefore natural to ask whether each traced
vertex has a nonzero geometric Gaussian approximation. The answer is
negative, even on positive paths with every crossing power equal to
three. This note proves that statement for the original finite vertex,
including the derivatives at the repeated spectral roots.

The exact Fourier representation itself is recalled from
[arbitrary-power source compilation](research_arbitrary_power_source_compilation.md),
§4. The new calculation is a two-variable factorial formula for the
traced power-three vertex and a proof of its endpoint asymptotic. The
failure concerns this particular local factorization. It does not
contradict the [complete internal-pair theorem](research_internal_pair_three_full_boundary_packet.md),
which integrates one more wire, or assert a failure of the volume
conjecture for the fully contracted source.


Sections 7--9 give a constructive follow-up: an explicit transformed
endpoint corner can be removed at every vertex with an exponentially
smaller error for each fixed complete-ended homogeneous chain. The
retained vertex has a nonzero holomorphic packet near the homogeneous
wire point. The exact factorial ratios also give a normalized retained array
that is almost invariant under one-step translations, with an explicit
nonzero Fourier coefficient. The complementary wire cycle and
full-chain coefficient remain separate.

## 1. The original traced vertex

Fix an integer \(N\ge2\), and put
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \kappa=q^{D^2/2},\qquad
 S_j=\prod_{\ell=1}^j2\sin(\pi\ell/N).
 \tag{1}
\]
The empty product \(S_0\) is one. In the original Newton basis
\(e_0,\ldots,e_D\), the trace pairing is
\(\phi(e_i e_j)=\delta_{i+j,D}\). Its matrix is the reversal matrix
\(J\). Multiplication by one positive physical crossing has matrix
\[
 M_{ij}=\kappa(-1)^i q^{i(j+1)}
             \frac{S_i}{S_jS_{i-j}}\quad(0\le j\le i<N),
 \qquad M_{ij}=0\quad(j>i).
 \tag{2}
\]
Multiplication is self-adjoint for this bilinear trace pairing:
\(M^T J=JM\). This statement concerns the bilinear form \(J\);
it is not a positive Hermitian unitarity statement.

The cardinal functions for the full half-band Fourier interpolation are
\[
 h_j(x)=\frac{\sin\bigl(\pi N(x-j/N)\bigr)}
                  {N\sin\bigl(\pi(x-j/N)\bigr)},\qquad
 \widetilde B_N(x,z)=\sum_{j=0}^D h_j(x)e_j(z).
 \tag{3}
\]
All apparent singularities in (3) are removable. At even \(N\) this
interpolation is antiperiodic with period one; no parity is discarded.
The degree-two traced vertex of power \(n\) is exactly
\[
 V_{n,N}(x,y)
 =\phi_z\!\left(R(z)^n\widetilde B_N(x,z)
                         \widetilde B_N(y,z)\right)
 =h(x)^TJM^nh(y).
 \tag{4}
\]
Thus (4) is an identity in the original algebra. It retains both values
and first normal derivatives at its double spectral roots.

## 2. An exact two-variable formula

Write
\[
 X=e^{2\pi ix},\qquad Y=e^{2\pi iy},\qquad
 c_x=\frac{e^{-\pi iDx}(1-X^N)}N,\qquad
 (a;r)_k=\prod_{\ell=0}^{k-1}(1-ar^\ell).
 \tag{5}
\]
In particular,
\(h_j(x)=c_x(-q^{-1})^j/(1-XQ^{-j})\).
We use
\({i\brack j}_Q=(Q;Q)_i/((Q;Q)_j(Q;Q)_{i-j})\)
for \(0\le j\le i<N\); these denominators are nonzero.

**Proposition 1.** For every \(N\ge2\),
\[
 V_{3,N}(x,y)=\kappa c_xc_y
 \sum_{\substack{i,j\ge0\\i+j<N}}
 \frac{X^iY^j(Q^{-1};Q^{-1})_{i+j}}
      {(X;Q^{-1})_{i+1}(Y;Q^{-1})_{j+1}}.
 \tag{6}
\]
The formula is initially read away from the displayed denominators;
after multiplication by \(c_xc_y\) its singularities are removable.
In the region \(|X|,|Y|<1\) no such interpretation is needed.

*Proof.* The finite \(Q\)-binomial identity gives
\[
 \sum_{j=0}^i
 \frac{(-1)^jQ^{j(j-1)/2}{i\brack j}_Q}{1-XQ^{-j}}
 =
 \frac{X^i(Q^{-1};Q^{-1})_i}{(X;Q^{-1})_{i+1}}.
 \tag{7}
\]
For completeness, multiplication by the denominator on the right
turns the left side into a polynomial of degree at most \(i\).
Its coefficients of degrees \(0,\ldots,i-1\) vanish, since the
corresponding Taylor sums before multiplication are
\((Q^{-r};Q)_i=0\) for \(0\le r<i\). The coefficient of \(X^i\)
is \((Q^{-i};Q)_i=(Q^{-1};Q^{-1})_i\). This proves (7).

Using
\({i\brack j}_Q=q^{j(i-j)}S_i/(S_jS_{i-j})\)
in (2) now gives the exact transformed vector
\[
 (Mh(x))_i=
 \kappa c_x(-q)^i
 \frac{X^i(Q^{-1};Q^{-1})_i}{(X;Q^{-1})_{i+1}}.
 \tag{8}
\]
Because \(M^T J=JM\), equation (4) for \(n=3\) equals
\((Mh(x))^TJM(Mh(y))\). Its \((i,j)\) entry is zero if
\(i+j>D\); otherwise
\[
 (JM)_{ij}=\kappa(-1)^{D-i}q^{(D-i)(j+1)}
                        \frac{S_{i+j}}{S_iS_j}.
 \tag{9}
\]
Substitution of (8) into (9) cancels the two separate sine
factorials. The remaining factor is
\((Q^{-1};Q^{-1})_{i+j}\). The constant phase reduces to
\(\kappa^3(-1)^Dq^D=\kappa\), since
\(\kappa^2=(-1)^Dq^{-D}\). This proves (6) at both parities.
\(\square\)

## 3. The entropy of the complete double sum

Let
\[
 X_*=\frac{1+i\sqrt3}{4},\qquad
 x_*=\frac16+\frac{i\log2}{2\pi};
 \qquad e^{2\pi ix_*}=X_*.
 \tag{10}
\]
Use the real function
\[
 \mathcal J(s)=\int_0^s\log(2\sin\pi u)\,du
 \quad(0\le s\le1)
 \tag{11}
\]
and put
\[
 L(s)=\int_0^s\log|1-X_*e^{-2\pi iu}|\,du.
 \tag{12}
\]
On the closed triangle \(s,t\ge0,\ s+t\le1\), define
\[
 H(s,t)=\mathcal J(s+t)-(s+t)\log2-L(s)-L(t).
 \tag{13}
\]
This is the exponential rate of the absolute value of the summand
in (6). It is essential to use this joint rate. Separate estimates
on the two vectors \(Mh(x)\) would lose the factor \(S_{i+j}\).

**Lemma 2.** The maximum of \(H\) on this triangle is zero,
attained only at \((0,0)\).

*Proof.* In the interior,
\[
 H_s=\log\frac{\sin\pi(s+t)}
                         {|1-X_*e^{-2\pi is}|},\qquad
 |1-X_*e^{-2\pi is}|^2
       =\frac54-\cos(\pi/3-2\pi s).
 \tag{14}
\]
At a critical point equality of the two denominators gives either
\(s=t\) or \(s+t=1/3\). In the latter case each denominator is
strictly smaller than \(\sqrt3/2\), so both derivatives
are positive. There is no critical point on that open segment.

On the diagonal \(s=t=a\), put \(r=\tan(\pi a)>0\). The sign
of \(H_s(a,a)\) is the opposite of the sign of
\[
 7r^4-4\sqrt3r^3-6r^2-4\sqrt3r+3
 =(r-\sqrt3)(7r^3+3\sqrt3r^2+3r-\sqrt3).
 \tag{15}
\]
The cubic factor is strictly increasing for \(r>0\), with a single
zero before \(\sqrt3\). Consequently \(H(a,a)\) first decreases,
then increases, then decreases. Its first stationary value is
negative; the only possible positive stationary value would be at
\(a=1/3\). In fact,
\[
 H(1/3,1/3)
 =-\mathcal J(1/3)-\frac23\log2+
       \frac{2}{\pi}\Im\operatorname{Li}_2(X_*)
 <-\frac{47}{1000}.
 \tag{16}
\]
Here \(L(1/3)=-\Im\operatorname{Li}_2(X_*)/\pi\), obtained by
integrating the absolutely convergent series for
\(\log(1-X_*e^{-2\pi iu})\). The strict rational inequality in
(16) is certified by interval arithmetic below.

On an axis let \(f(s)=H(s,0)\). The sign of \(f'(s)\) is the
sign of
\(-3/4+(\sqrt3/2)\sin(2\pi s)\).
It is negative on \((0,1/6)\), positive on \((1/6,1/3)\),
and negative on \((1/3,1)\). Moreover,
\[
 f(1/3)=\frac{H(1/3,1/3)+3\mathcal J(1/3)}2<0,
 \qquad f(1)=-\log2.
 \tag{17}
\]
We used \(\mathcal J(1/3)<-1/10\) and \(L(1)=0\); the latter
also follows from the convergent logarithmic series.
Thus both axes are strictly negative away from their common origin.

Finally, on \(s+t=1\), equation (13) becomes
\(-\log2-L(s)-L(1-s)\). The integrand in (12) is at least
\(-\log2\), with equality only at isolated points. Its integral
over any interval of positive length is therefore strictly larger
than that constant lower bound. This proves \(H<0\) on the top
edge. Compactness and the preceding classification of all interior
critical points prove the lemma. \(\square\)

## 4. The actual endpoint asymptotic

**Theorem 3.** There is a fixed complex neighborhood of
\((x_*,x_*)\) on which, along the full sequence of levels,
\[
 V_{3,N}(x,y)=
 \frac{\kappa e^{-\pi iD(x+y)}(1-X^N)(1-Y^N)}
      {N^2(1-X)(1-Y)}
 \left(1+O(N^{-1})\right).
 \tag{18}
\]
The error is uniform on a smaller fixed neighborhood. Every fixed
complex derivative of the relative error is also \(O(N^{-1})\)
after shrinking that neighborhood.

*Proof.* Let \(T_{ij}\) denote the summand in (6).
The elementary uniform sine-factorial estimate and the smooth
Riemann-sum estimate for the denominator give
\[
 \log|T_{ij}|=NH(i/N,j/N)+O(\log N)
 \tag{19}
\]
at \(X=Y=X_*\), uniformly for \(i+j<N\). The sine estimate
includes the endpoints: subtracting
\(\log u+\log(1-u)\) from \(\log(2\sin\pi u)\) leaves a
smooth function, and the two remaining sums are estimated by
factorials. This yields the stated uniform logarithmic error.
The denominator has no zero because \(|X_*|=1/2\).

Fix \(\delta=1/100\). Lemma 2 and compactness give a strict
negative upper bound for \(H\) when \(s+t\ge\delta\).
That bound persists when \(X\) and \(Y\) vary in a sufficiently
small fixed complex neighborhood of \(X_*\). Indeed the general
rate is the continuous function
\[
 \mathcal J(s+t)+s\log|X|+t\log|Y|
 -\int_0^s\log|1-Xe^{-2\pi iu}|\,du
 -\int_0^t\log|1-Ye^{-2\pi iu}|\,du.
 \tag{20}
\]
The sum of the terms with \(i+j\ge\delta N\) is consequently
bounded by a polynomial in \(N\) times \(e^{-\varepsilon N}\).

Shrink the neighborhood so that \(|X|,|Y|\le r=3/5\).
For \(k=i+j\le\delta N\),
\[
 |T_{ij}|\le (1-r)^{-2}
                 \left(\frac r{1-r}\right)^k S_k,\qquad
 S_k\le \frac{2\pi}{N}(2\pi\delta)^{k-1}\quad(k\ge1).
 \tag{21}
\]
Since \(2\pi\delta\,r/(1-r)<1\), summing (21), with \(k+1\)
pairs at a given \(k\), gives \(O(N^{-1})\) for all these
terms except \(k=0\). The latter is exactly
\(1/((1-X)(1-Y))\). This proves (18) by (6). Uniform
holomorphy and Cauchy's estimate give the derivative statement.
\(\square\)

## 5. Comparison with the geometric vertex

The homogeneous positive unit-charge point for a degree-two path
with every power equal to three was established in
[the bare-kernel obstruction](research_bare_kernel_power_three_obstruction.md),
§2. In the present notation it is
\[
 \cos t_*=-\frac14+\frac{3\sqrt3}{4}i,\qquad
 t_*=1.7227684498\ldots-1.0870701449\ldots i,
 \qquad
 3t_*+4i\operatorname{arsinh}(\sin(t_*/2))=2\pi.
 \tag{22}
\]
Its stationary wire coordinate is exactly the \(x_*\) in (10):
\[
 \sin(\pi x_*)=\frac{\cos(t_*/2)}{\sqrt2}.
 \tag{23}
\]
All branches here are the positive geometric branches used in the
cited note.

Continue \(\mathcal J\) holomorphically from \((0,1)\) to the
vertical strip \(0<\Re z<1\), with derivative
\(\log(2\sin\pi z)\). The geometric contribution of a fixed
wire and a vertex angle is
\[
 b(x,t)=-\mathcal J(1/2-x+t/(2\pi))
        -\mathcal J(1/2-x-t/(2\pi))-2\mathcal J(x).
 \tag{24}
\]
This is the usual factorial phase; the two omitted initial terms
\(\mathcal J(1/2+t/(2\pi))+
\mathcal J(1/2-t/(2\pi))\) sum to zero on these branches.
At (22) the two shifted arguments in (24) have real parts
larger than \(1/20\), so no branch-boundary issue enters.
The proposed geometric vertex action is
\[
 F_*=2b(x_*,t_*)+\frac{3it_*^2}{4\pi}-it_*.
 \tag{25}
\]
The same scalar certificate proves
\[
 \Re F_*=0.6461318944\ldots,\qquad
 \log2-\Re F_*>\frac{47}{1000}.
 \tag{26}
\]
But Theorem 3 gives
\[
 \lim_{N\to\infty}\frac1N
       \log|V_{3,N}(x_*,x_*)|=\log2.
 \tag{27}
\]
Thus this exact traced vertex does not have a leading packet with
action \(F_*\). The discrepancy survives in an open neighborhood,
by (18), continuity of the geometric data, and the strict gap (26).

This neighborhood also occurs in finite original paths.
The proof of Corollary 4 in the cited bare-kernel note gives a
bound, independent of path length, on the sum of squared distances
of all edge square coordinates from their homogeneous values.
Sum the distances of the two edges adjacent to each internal
vertex. Every edge is counted at most twice. Hence some internal
vertex has both adjacent edges at distance \(O(m^{-1/2})\) from
their homogeneous values as the number \(m\) of selected vertices
grows. The inverse square map and the stationary wire coordinates
are smooth at the fixed positive point. Both actual wire
coordinates at these vertices therefore tend to \(x_*\), and the
vertex angle tends to \(t_*\). For sufficiently large finite
paths the same local obstruction applies. The carrier, primitive
slope and component conditions remain those of the original path.

The conclusion is specific: grouping the trace at each vertex
does not, by itself, produce geometric local asymptotics on all
positive three-crossing paths. A successful composition argument
must still control cancellation between these endpoint
contributions after the remaining wire integrations.

One exact calculation explains why the local rate cannot simply be
added over vertices. The leading term in (18) is
\(\kappa h_0(x)h_0(y)\), whereas the next wire contraction satisfies
\[
 N\int_0^1 h_0(x)^2\,dx=1,\qquad
 h_0(x)=\frac1N\sum_{k=0}^{D}
                    e^{2\pi i(k-D/2)x}.
\]
The identity follows by extracting the constant Fourier coefficient:
there are exactly \(N\) pairs of indices with sum \(D\).
It also holds on any horizontal translate of the integration interval,
because \(h_0^2\) is entire and one-periodic. Thus an exponentially
large local value on a complex contour can have a bounded exact
contraction. This calculation does not bound the other sectors of the
full path; it identifies the cancellation which a global proof must
respect.

## 6. Reproduction

Run

    python3 experiments/check_traced_three_vertex_endpoint.py

The [checker](../experiments/check_traced_three_vertex_endpoint.py)
uses Arb at 160 bits to prove the five strict scalar inequalities
in (16), (17), (24) and (26). It evaluates the analytic primitive as
\[
 \mathcal J(z)=
 -\frac{i\pi}{2}(z^2-z)
 +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iz})
 -\frac{i\pi}{12}.
 \tag{28}
\]
On the specified strip this is the continuation of (11), with the
branches fixed above.

Separately, 351 numerical diagnostics at 80 decimal digits compare
(8) and (6) against the sine-factorial matrix (2) and the original
cardinal functions (3), at levels 2 through 14 and three pairs of
complex arguments. Both parities are included. These finite checks
test the exact formulas and their normalization; the proofs of
Lemma 2 and Theorem 3 give the asymptotic conclusion.
The saved [result](../repro/results/research-traced-three-vertex-endpoint.json)
records the script hash, interval enclosures and finite-check errors.

## 7. Removing the endpoint corner after the original chain contraction

The large local endpoint in Theorem 3 can be removed with an
exponentially smaller error in every fixed complete-ended homogeneous
three-crossing chain. The removal below is an exact change of its
Fourier density whose source error is estimated after contraction.
It is not a claim that the removed density is pointwise small.

Put
\[
 \epsilon=\frac1{50},\quad L=\lfloor\epsilon N\rfloor,
 \quad P_L=\operatorname{diag}(\mathbf1_{0\le j\le L}),
 \quad A=JM^3,
 \quad E_L=M^TP_LJM P_LM,
 \quad \widetilde A=A-E_L.
 \tag{29}
\]
Since \(2L\le D\), the matrix \(P_LJM P_L\) includes exactly
all terms \(0\le i,j\le L\) of (6). Consequently
\(h(x)^T\widetilde Ah(y)\) is that actual finite double sum
with this entire corner removed. Every remaining factorial,
phase, and half-band cardinal factor is unchanged. The matrix is
still symmetric; its composition uses the same exact cardinal
averaging as the original vertex.

**Proposition 4.** Let \(c=2\mathcal J(5/6)\),
\(M_\infty=4G/\pi\), and fix \(m\ge1\). Define
\[
 S_{m,N}(z,w)=v(z)^TA^mv(w),\qquad
 \widetilde S_{m,N}(z,w)=v(z)^T\widetilde A^mv(w),
 \qquad v(z)=(e_0(z),\ldots,e_D(z))^T.
 \tag{30}
\]
For every fixed pair of nonnegative integers \(a,b\), at both
parities and along the full sequence of levels,
\[
 \sup_{z,w\in[-2,2]}
 \left|\partial_z^a\partial_w^b
        (S_{m,N}-\widetilde S_{m,N})(z,w)\right|
 \le C N^A
   \exp N\left\{(2m-1)c+M_\infty+\frac3{25}\right\}.
 \tag{31}
\]
The constants may depend on \(m,a,b\). For complex boundary
angles, add \(|\Im u|+|\Im v|\) to the exponent, with
\(z=-2\cos u,w=-2\cos v\). The mirrored statement also holds.

*Proof.* The original braid and positive similarity give
\[
 MAM^{-1}=\kappa H,\quad H=M^*M,\qquad
 M E_L M^{-1}=\kappa J M^{-1}P_LJM P_L.
 \tag{32}
\]
For the second identity, use
\(MM^T=MJMJ=\kappa JM^{-1}\). We bound the two short-index
factors in (32) separately. For \(j\ge k\), \(k\le L\),
\[
 |(M^{-1})_{jk}|=\frac{S_j}{S_kS_{j-k}}
 \le\frac{2^k}{S_k}
 \le\frac{(N/2)^k}{k!}.
 \tag{33}
\]
Here \(M^{-1}=\overline M\), and
\(2\sin(\pi r/N)\ge4r/N\) for \(1\le r\le L\).
The displayed bound increases with \(k\le L\). For
\(0\le i,j\le L\), the decreasing function \(\sin x/x\)
on \((0,\pi)\) gives
\[
 |(JM)_{ij}|=\frac{S_{i+j}}{S_iS_j}
 \le {i+j\choose i}\le 2^{2L}.
 \tag{34}
\]
Norms of matrices with these dimensions add only powers of \(N\).
The inequality \(L!\ge(L/e)^L\), with the \(L=0\) case
read separately, proves
\[
 \|M E_LM^{-1}\|
 \le C N^A\exp\{N\sigma\},\qquad
 \sigma=\frac1{50}\log(100e)<\frac3{25}.
 \tag{35}
\]
Indeed \(e^5>100\). The established original one-crossing
operator estimate gives \(\|M\|\le C e^{Nc}\), hence
\(\|H\|\le C e^{2Nc}\); see
[the Gaussian operator limit](research_one_crossing_gaussian_window.md),
Sections 4--5. Since \(\sigma<3/25<2c\), a fixed product
with \(r\ge1\) corner matrices and \(m-r\) original vertex
matrices has, in the \(M\)-similarity gauge, norm at most
\[
 C_mN^{A_m}
      \exp N\{2(m-r)c+r\sigma\}.
 \tag{36}
\]
This also bounds products of \(A\) and \(\widetilde A\)
with one specified \(E_L\), by expansion or telescoping.

It remains essential to restore the original boundary observations.
At every double physical root, the exact inverse-crossing identity
for both value and first normal is
\[
 (v^TM^{-1})^{(\nu)}(c_a)
 =\sum_{j=0}^{\nu}{\nu\choose j}
       (R^{-1})^{(\nu-j)}(c_a)v^{(j)}(c_a)^T,
       \qquad \nu=0,1.
 \tag{37}
\]
At the odd simple root only \(\nu=0\) is used. The original
full-Hermite bounds give
\(\|v^{(\nu)}(c_a)\|\le CN^A e^{NM_\infty/2}\)
and polynomial inverse-crossing jets. The right observation obeys
\(\|Mv^{(\nu)}(c_b)\|\le CN^A e^{N(c+M_\infty/2)}\).
Thus (36) has physical mixed-jet rate
\((2m-2r+1)c+r\sigma+M_\infty\), largest at \(r=1\).
These are the literal first normals, not values of an arbitrary
interpolant. The detailed Hermite bounds and exact identity (37)
are proved in
[the open-source spectral estimate](research_positive_three_crossing_cycle.md),
Proposition 8.

Both polynomials in (30) have degree at most \(N-1\) in each
boundary variable, independently of \(m\). The polynomial norm
bound for full physical Hermite interpolation therefore extends
these jet estimates to the real square. Markov's inequality supplies
all fixed higher ordinary derivatives. The usual Laurent-polynomial
bound of degree \(N-1\) in each angular variable supplies the
stated complex-angle cost. This proves (31), including even-level
complete colors, without treating \(-2\) as a physical node there.
\(\square\)

**Corollary 5.** Let \(M_m\) be the actual positive geometric action
of the original path of \(m\) selected power-three vertices with
two complete outside endpoints. Then
\[
 M_m>(2m-1)c+M_\infty+\frac3{25}+\frac1{15}.
 \tag{38}
\]
Consequently (31) is strictly below the geometric rate, with the
uniform positive margin \(1/15\), for every fixed \(m\).
This remains true on a sufficiently small complex neighborhood of
the two complete outside colors and for all fixed ordinary normals.

*Proof.* Use the positive homogeneous point \(t_*=a-iH\) in
Section 5, and put \(g=(3a-2\pi)/4\). The exact calibration
of its original eight tetrahedra proves
\(\Re F_*=2c\); see
[the homogeneous action calculation](research_homogeneous_three_action_calibration.md).
The original edge energy is therefore
\(\pi(M_\infty-2c)\). Assign \(s=a,g=g\) to both
incidences of every selected vertex, and \(s=g=0\) at the two
outside vertices. This is precisely the strict feasible trial in
[the finite-path realization](research_bare_kernel_power_three_obstruction.md),
Section 4. Its internal edges are homogeneous. Each attaching edge
has energy
\[
              F_{\rm att}=8E(a/4,g/2)<1.
 \tag{39}
\]
Here is an elementary bound independent of numerical integration.
The exact homogeneous cosine and height give
\(3/2<\cosh H<7/4\) and
\(a=\pi/2+\arcsin(1/(4\cosh H))\). In particular
\(a>25/16+1/7>17/10\), while
\(a<11/7+17/100<7/4\), using
\(\arcsin(1/6)<17/100\). Thus \(a/4<7/16\), and
\(0<|g|/2<3/20\), using \(\pi<22/7\).
The square-energy inequality
\(E(A,y)\le E(A,0)+E(0,y)\), its even symmetries, and the
axis interpolation bound in
[the radical energy comparison](research_radical_path_sector_gap.md),
(17)--(18), give
\[
 \begin{split}
 E(a/4,g/2)
 &<\frac{(7/16)^2}{24}
               \left(5+6\frac{10}{9}+\frac85\right)
       +\frac12\left(\frac3{20}\right)^2\frac{21}{20}\\
 &=\frac{270991}{2304000}<\frac18.
 \end{split}
 \tag{40}
\]
The only secant bounds used here are
\(\sec(7/16)<10/9\), \(\sec(7/8)<8/5\), and
\(\sec(3/10)<21/20\), each following from the alternating
cosine Taylor lower bound.

The variational minimum/action identity for the original complete
path now yields
\[
 M_m\ge 2mc+2M_\infty-2c-\frac{2F_{\rm att}}\pi.
 \tag{41}
\]
There are \(m-1\) internal edges and two attaching edges, including
when \(m=1\). The strict positive minimizer and this identity are
established in the
[edge-cut energy comparison](research_edge_cut_energy_comparison.md).
Finally the existing bounds
\(M_\infty>29/25\), \(8/25<c<1/3\), and \(\pi>25/8\)
give
\[
 M_\infty-c-\frac{2F_{\rm att}}\pi-\frac3{25}
 >\frac{29}{25}-\frac13-\frac{16}{25}-\frac3{25}
 =\frac1{15}.
 \tag{42}
\]
This proves (38). Boundary continuity of the positive point and the
explicit complex-angle cost in Proposition 4 give the final local
statement. \(\square\)

The result deletes a whole transformed endpoint corner before the
remaining Fourier integrations, at every vertex at once. It is
compatible with the exponentially large pointwise endpoint in
Theorem 3 because the estimate uses the exact original boundary
observations after contraction. It does not yet prove a nonzero
geometric coefficient for \(\widetilde S_{m,N}\), nor does it
make its mixed spectral weights nonnegative.

The focused
[corner checker](../experiments/check_three_vertex_corner_deletion.py)
and its [record](../repro/results/research-three-vertex-corner-deletion.json)
verify the rational bounds in (35), (39)--(42) and independent finite
matrix/Fourier identities for (29), (32). Finite diagnostics are only
normalization checks; the estimates above are uniform proofs.

## 8. A nonzero geometric-rate saddle in the retained vertex

The later [global retained-wire bound](research_three_vertex_global_wire_bound.md)
proves that this saddle is the unique absolute entropy maximum over
the full common-height Fourier torus. Its cyclic and fixed-Fourier-endpoint
consequences retain the distinction from actual ordinary-color caps.

The retained corner complement has a genuine stationary contribution
at the homogeneous wire point. This is a statement about the modified
finite vertex (29), not a deduction of a full-chain coefficient.
Section 9 proves the accompanying fixed-neighborhood packet.

**Proposition 6.** With \(x_*\) from (10), the exact corner-deleted
vertex satisfies
\[
 h(x_*)^T\widetilde Ah(x_*)
 =\kappa\,\frac{2}{3^{1/4}\sqrt{2+i\sqrt3}}
       N^{-1/2}e^{2cN}\{1+O(N^{-1})\}.
 \tag{43}
\]
The square root has positive real part. The statement includes both
parities and every level, without restricting \(N\) modulo three.

*Proof.* In (6) write \(s=i/N,t=j/N\). The real summand entropy
is the same \(H(s,t)\) as in (13). On the limiting closed triangle
with \([0,1/50]^2\) removed, its unique maximum is
\((s,t)=(1/3,1/3)\). We verify the additional boundary comparisons
needed beyond Lemma 2.

On a new cut face \(s=1/50,0\le t\le1/50\), equation (14)
gives \(H_t<0\), since its numerator is at most
\(\sin(\pi/25)<1/2\) and its denominator is at least \(1/2\).
Thus its maximum is at \((1/50,0)\), and
\[
 H(1/50,0)\le\mathcal J(1/50)<-\frac3{50}
                  < 2c-\log2=H(1/3,1/3).
 \tag{44}
\]
The first bound uses \(L(s)\ge-s\log2\). For the second,
\(2\sin\pi s\le2\pi s\) gives
\(\mathcal J(1/50)\le[\log(\pi/25)-1]/50\);
\(\pi e^2<25\) suffices. The final inequality follows from
\(c>8/25\) and \(\log2<7/10\).
The other cut face is symmetric. Moving its finite-level boundary
by \(O(N^{-1})\) preserves a strict gap.

On each remaining coordinate axis, the maximum is among the cut
endpoint, \(1/3\), and \(1\), by the derivative classification
in Lemma 2. Formula (17), \(3\mathcal J(1/3)=-c\), and
\(\log2<3c\) put the middle candidate strictly below
\(H(1/3,1/3)\). The endpoint value \(-\log2\) is smaller too.
For the top edge, the convergent Fourier primitive gives
\( |L(s)|\le\operatorname{Li}_2(1/2)/\pi<3/(5\pi)\).
Indeed the first two series terms and the remaining geometric tail
give \(\operatorname{Li}_2(1/2)\le1/2+1/16+1/36<3/5\).
Hence the top edge has
\(H<-\log2+6/(5\pi)<-4/15\), using
\(\log2>2/3\) and \(\pi>3\). The classification of all
interior stationary points in Lemma 2 completes the unique-maximum
proof. Uniform sine-factorial estimates make every summand outside
any fixed neighborhood of this maximum exponentially smaller,
including the original finite endpoints.

For the complex phase, fix the continuous logarithm with
\(\log X_*=-\log2+i\pi/3\), and set
\[
 I(s)=\int_0^s\log(1-X_*e^{-2\pi iu})\,du,
 \quad F(s,t)=\mathcal J(s+t)
    +\frac{i\pi}{2}\{s+t-(s+t)^2\}
    +(s+t)\log X_*-I(s)-I(t).
 \tag{45}
\]
Its real part is \(H\). Direct differentiation gives
\[
 e^{F_s}=
   \frac{X_*(1-e^{-2\pi i(s+t)})}{1-X_*e^{-2\pi is}},
 \qquad
 F_s(1/3,1/3)=F_t(1/3,1/3)=0,
 \quad
 F''=-\pi
 \begin{pmatrix}
  \sqrt3+i&1/\sqrt3+i\\
  1/\sqrt3+i&\sqrt3+i
 \end{pmatrix}.
 \tag{46}
\]
The zero logarithms in (46) follow directly from (45), or from the
arguments \(\pi/3-\pi/6-\pi/6=0\). Thus an integer logarithmic
ambiguity is not inferred away. The real Hessian is strictly
negative definite, and
\(\det(-F'')=(4\pi^2/3)(2+i\sqrt3)\).

Uniform sine-factorial asymptotics and Euler--Maclaurin for the
nonvanishing denominator products give, near this fixed point, the
summand in (6) without its outside \(\kappa c_xc_y\) factor as
\[
 N^{1/2}g(s,t)e^{NF(s,t)}\{1+O(N^{-1})\},\qquad
 g(s,t)=
 \frac{\sqrt{2\sin\pi(s+t)}\,e^{-i\pi(s+t)/2}}
 {(1-X_*)\sqrt{(1-X_*e^{-2\pi is})(1-X_*e^{-2\pi it})}}.
 \tag{47}
\]
All square roots continue from the positive sine-factorial factor
and the denominator product. At the saddle,
\(g_*=(4/3)3^{1/4}e^{-i\pi/3}\). The two-dimensional lattice
Gaussian therefore contributes
\(2\pi N^{3/2}g_*e^{NF_c}/\sqrt{\det(-F'')}\), with relative
error \(O(N^{-1})\). The first correction of order \(N^{-1/2}\)
is odd; summation of its shifted Gaussian lattice has vanishing
integral and exponentially small discretization error. This also
explains why no condition on \(N\bmod3\) appears.

Here \(F_c=F(1/3,1/3)\), and \(I(1/3)\) is real: its integrand pairs with its complex
conjugate under \(u\mapsto1/3-u\). Thus
\(\Im F_c=\pi/3\). The exact entropy identity in
[the positive three-crossing calculation](research_positive_three_crossing_cycle.md),
(14a)--(14b), gives
\(F_c-\log X_*=2c\). Finally
\(c_{x_*}^2=N^{-2}X_*^{1-N}(1-X_*^N)^2\), with
\(|X_*|=1/2\). Combining the scalar factors in (47) gives exactly
\(2/(3^{1/4}\sqrt{2+i\sqrt3})\), proving (43).
\(\square\)

A point asymptotic does not justify differentiation into a fixed
complex neighborhood of the wire parameters. Such a neighborhood
requires an analytic lattice-contour argument with the exact finite
source or an exponentially accurate analytic interpolation. Nor does
(43) alone control the remaining full wire integrals of an arbitrary
chain. Proposition 4 supplies the global error estimate needed to
make that next analysis apply to the original source.

## 9. A fixed complex neighborhood of the retained packet

The exact finite products admit an analytic interpolation on a local
index rectangle. This supplies the missing uniformity in the last
paragraph of Section 8; it still does not estimate the full remaining
wire cycle of an arbitrary chain.

**Theorem 7.** There is a fixed complex neighborhood \(\mathcal U\)
of \((x_*,x_*)\), and holomorphic functions \(\Phi,a\) on it,
with \(a\) nowhere zero, such that
\[
 h(x)^T\widetilde A h(y)
 =\kappa N^{-1/2}a(x,y)e^{N\Phi(x,y)}
                         \{1+O_{\mathcal U}(N^{-1})\}.
 \tag{48}
\]
The error is holomorphic and uniform on a slightly larger neighborhood
than any chosen compact subset of \(\mathcal U\), so its fixed
parameter derivatives have the same order after factoring the displayed
packet. At the central point,
\(\Phi(x_*,x_*)=2c\) and
\(a(x_*,x_*)=2/(3^{1/4}\sqrt{2+i\sqrt3})\).
The theorem holds at both parities and all sufficiently large levels.

*Proof.* Put \(X=e^{2\pi ix},Y=e^{2\pi iy}\), and keep the
branches \(\log X=2\pi ix,\log Y=2\pi iy\) near (10).
For \(|X|<1\), define
\[
 \mathcal L_N(s;X)=
 -\sum_{\substack{k\ge1\\N\nmid k}}
 \frac{X^k\{1-e^{-2\pi ik(s+1/N)}\}}
             {k(1-e^{-2\pi ik/N})}
 +(s+1/N)\log(1-X^N e^{-2\pi iNs}).
 \tag{49}
\]
This is the length-\(s+1/N\) logarithm in
[the exact root-product interpolation](research_root_pochhammer_interpolation.md),
Propositions 1--2; it also satisfies its exact off-grid difference
equation. The series is locally normally convergent wherever
\(|X|e^{2\pi\Im s}<1\). At every nonnegative integer \(i\),
\[
 \mathcal L_N(i/N;X)
       =\log\prod_{\ell=0}^{i}(1-Xe^{-2\pi i\ell/N}),
 \tag{50}
\]
with the logarithm equal to the sum of the convergent individual
logarithmic series. Indeed the nonresonant \(k\) terms sum a
geometric progression. For \(k=aN\), the original logarithmic
sum is \(-(i+1)X^{aN}/(aN)\); these are exactly the final term
in (49). Thus (49) retains the finite-root resonance rather than
replacing it by a non-root product.

Let \(G_N\) be the exact sine-factorial interpolation in
[the original complex-factorial theorem](exact_factorial_interpolation_and_complex_contours.md),
Sections 1 and 4. It satisfies \(G_N(k)=S_k\) and, on compact
subsets of \(0<\Re z<1\),
\(G_N(Nz)=\sqrt{2N\sin\pi z}\,e^{N\mathcal J(z)}
(1+O(N^{-1}))\), holomorphically with every fixed derivative.
Consequently
\[
 \begin{split}
 \mathcal T_N(s,t;X,Y)
 ={}&X^{Ns}Y^{Nt}
    e^{i\pi N\{s+t-(s+t)^2\}/2-i\pi(s+t)/2}\,
    G_N(N(s+t))\\
 &\hspace{12mm}\cdot
       e^{-\mathcal L_N(s;X)-\mathcal L_N(t;Y)}
 \end{split}
 \tag{51}
\]
is an exact analytic interpolation of each summand in (6) near
\((s,t)=(1/3,1/3)\), with its original phase. In particular
it matches the full source already traced in (4), not merely a
collection of value-only ordinary-color samples.

For clarity the uniform asymptotic of (49) also follows directly
from its series. On a smaller fixed strip choose \(r<1\) with
\(\max(|X|,|X|e^{2\pi\Im s})\le r\).
For nonresonant \(k\),
\(|1-e^{-2\pi ik/N}|\ge4/N\). Terms \(k\ge N/2\)
are therefore exponentially small, including after any fixed
derivative, and the resonant logarithm has the same property.
For \(k<N/2\), expand
\((1-e^{-2\pi ik/N})^{-1}=N/(2\pi ik)+1/2+O(k/N)\).
The remainders are summable against \(r^k\). Expansion of
\(e^{-2\pi ik/N}\) in the numerator gives
\[
 \mathcal L_N(s;X)
 =N I_X(s)+\tfrac12\log(1-X)
             +\tfrac12\log(1-Xe^{-2\pi is})+O(N^{-1}),
 \quad I_X(s)=\int_0^s\log(1-Xe^{-2\pi iu})\,du.
 \tag{52}
\]
It holds holomorphically with fixed derivatives. Formula (51) thus
has the uniform analytic symbol
\(N^{1/2}g(s,t;X,Y)e^{NF(s,t;X,Y)}(1+O(N^{-1}))\), where
\[
 \begin{split}
 F={}&\mathcal J(s+t)+\frac{i\pi}{2}\{s+t-(s+t)^2\}
                  +s\log X+t\log Y-I_X(s)-I_Y(t),\\
 g={}&\frac{\sqrt{2\sin\pi(s+t)}e^{-i\pi(s+t)/2}}
 {\sqrt{(1-X)(1-Xe^{-2\pi is})
                (1-Y)(1-Ye^{-2\pi it})}}.
 \end{split}
 \tag{53}
\]
All branches agree with (47). The implicit-function theorem and
(46) provide a unique holomorphic critical point
\((s_c,t_c)\) near \((1/3,1/3)\); its Hessian stays
nondegenerate and has strictly negative real part.

Here are the finite-cycle estimates which justify using that
critical point. Choose a small fixed real rectangle centered at
\((1/3,1/3)\), contained in the interior of the retained triangle.
The strict global entropy comparison in Proposition 6 supplies a
positive gap outside this rectangle. Uniform logarithmic estimates
for the original sine products and their nonzero denominator products
make this an actual finite-sum bound, up to polynomial factors.
It persists under a sufficiently small complex change of \(X,Y\),
by compactness and continuity. No approximate interpolation is used
on this exterior set.

For the lattice sum inside the rectangle, move each real endpoint to
a neighboring midpoint between lattice nodes and use the exact product
of the two cotangent residue kernels \(\pi N\cot(\pi Ns)\) and
\(\pi N\cot(\pi Nt)\), with (51). Choose the rectangle small
enough that \(|F_s|,|F_t|<\pi/2\) on a complex neighborhood.
Choose its upper and lower contour heights \(h>0\) sufficiently
small compared with its real half-width. The real Hessian in (46)
then gives a strict gap on every vertical side, uniformly for both
other-coordinate heights in \([-h,h]\). This remains true for
nearby parameters and midpoint endpoints. Shrink \(\mathcal U\)
again so \(|\Im s_c|,|\Im t_c|<h/4\).

On each horizontal side the cotangent is its constant \(\mp i\)
plus a term bounded by \(C e^{-2\pi Nh}\). Displacing a phase
in either imaginary direction by at most \(h\) costs at most
\(\pi Nh/2\), by the gradient bound; the real-slice maximum
and the critical real action are arbitrarily close as the parameter
neighborhood shrinks. Thus every nonconstant cotangent term has a
strict exponential gap. The vertical sides have the preceding
Hessian gap, with bounded cotangent at the midpoint real coordinate.
Their products and intersections retain one of these strict gaps.
The constant-cotangent terms combine, with the original orientations,
into \(N^2\) times one ordinary double integral. The constant is
one: it is the same residue normalization that sums each enclosed
lattice point with coefficient one. Its contour can be moved to the
horizontal plane through \((s_c,t_c)\); all connecting side
integrals retain the vertical-side gap. On that plane strict real
concavity gives its unique maximum at the critical point. This
accounts for every part of the local original lattice cycle.

The uniform two-dimensional Gaussian formula now applies to (53).
The leading coefficient and phase in (48) are exactly
\[
 \Phi=F(s_c,t_c;X,Y)-\tfrac12(\log X+\log Y),
 \qquad
 a=\frac{2\pi\sqrt{XY}\,g(s_c,t_c;X,Y)}
                      {\sqrt{\det(-F''(s_c,t_c;X,Y))}}.
 \tag{54}
\]
The determinant square root continues from (46). Every factor is
nonzero on a smaller fixed neighborhood. The finite outside factors
\((1-X^N)(1-Y^N)\) have exponentially small relative effect.
The analytic symbol and the odd cancellation of the first Gaussian
correction give relative \(O(N^{-1})\); Cauchy's formula on a
smaller parameter neighborhood gives the claimed derivative statement.
At the central point (54) is precisely (43). \(\square\)

This proves a local holomorphic packet for the corner-deleted original
vertex, and Proposition 4 bounds its modification after any fixed
homogeneous open-chain contraction. The remaining task is to control
the complementary wire contours of that contracted chain and to
identify its global nonzero coefficient. Those conclusions do not
follow merely by multiplying (48) over the vertices.

## 10. Almost-invariant translations and an actual Fourier coefficient

The retained source now gives a precise version of the Fourier
analogy. The almost-invariance comes from its exact factorial ratios
near the selected stationary point. Its nonzero coefficient comes
from the computed Gaussian integral; almost-invariance alone would
not establish that coefficient.

For \(X=X_*\), define an array on \((\mathbb Z/N\mathbb Z)^2\)
using the representatives \(0\le i,j<N\):
\[
 a_N(i,j)=
 \begin{cases}
 \displaystyle
 \frac{X_*^{i+j}(Q^{-1};Q^{-1})_{i+j}}
 {(X_*;Q^{-1})_{i+1}(X_*;Q^{-1})_{j+1}},
   &i+j<N,\ \max(i,j)>L,\\[2mm]
 0,&\text{otherwise},
 \end{cases}
 \quad f_N=\frac{a_N}{\|a_N\|_{\ell^2}}.
 \tag{55}
\]
The source scalar is exactly
\(h(x_*)^T\widetilde Ah(x_*)=\kappa c_{x_*}^2\sum a_N\).
Let \(T_1,T_2\) denote cyclic one-step translations in the two
index coordinates. Define the unitary discrete Fourier transform by
\[
 \widehat f_N(k,\ell)=\frac1N
       \sum_{i,j=0}^{N-1}f_N(i,j)
                     e^{-2\pi i(ik+j\ell)/N}.
 \tag{56}
\]

**Corollary 8.** At both parities,
\[
 \|T_1f_N-f_N\|_2+\|T_2f_N-f_N\|_2=O(N^{-1/2}),
 \qquad
 |\widehat f_N(0,0)|
   =\left(\frac{24}{7}\right)^{1/4}N^{-1/2}
                       \{1+O(N^{-1})\}.
 \tag{57}
\]
Equivalently \(|\sum a_N|/\|a_N\|_2
=(24/7)^{1/4}\sqrt N\{1+O(N^{-1})\}\).
Thus the specified Fourier coefficient loses only a polynomial
factor relative to the actual retained coefficient norm.

*Proof.* Wherever two adjacent entries are in the retained support,
the original finite product gives exactly
\[
 \frac{a_N(i+1,j)}{a_N(i,j)}
 =\frac{X_*(1-Q^{-(i+j+1)})}{1-X_*Q^{-(i+1)}}.
 \tag{58}
\]
The analogous ratio holds in the other coordinate. At
\(i/N=j/N=1/3\) its limiting value is one by (46).
On a fixed small neighborhood of this point the denominator is
bounded away from zero, so the difference of the ratio from one
is at most
\(C(|i-N/3|+|j-N/3|+1)/N\).
The entropy gap in Proposition 6 makes the squared norm outside
that neighborhood exponentially smaller than the whole norm.
Every zero-extension or cyclic-boundary jump lies in this gapped
part, including the removed corner and the edge \(i+j=N-1\).
The local Gaussian estimate gives
\(\sum[(i-N/3)^2+(j-N/3)^2]|a_N(i,j)|^2
\le CN\|a_N\|_2^2\). Squaring this difference estimate, summing, and adding
those exponentially small boundary jumps proves the first assertion.

For the coefficient, put
\(B=-\Re F''\), \(C=-F''\), with the Hessian in (46).
The same lattice Gaussian, now applied to the squared absolute
summands, gives
\[
 \begin{split}
 \|a_N\|_2
 &=\frac{\sqrt\pi\,|g_*|}{(\det B)^{1/4}}
      N e^{NH_*}\{1+O(N^{-1})\},\\
 \left|\sum a_N\right|
 &=\frac{2\pi|g_*|}{|\sqrt{\det C}|}
      N^{3/2}e^{NH_*}\{1+O(N^{-1})\},\\
 \det B&=\frac{8\pi^2}{3},\qquad
 \det C=\frac{4\pi^2}{3}(2+i\sqrt3),\qquad
 H_*=2c-\log2.
 \end{split}
 \tag{59}
\]
The first Gaussian is positive; the second is the nonzero complex
Gaussian already computed in Proposition 6. Dividing the two
expressions and using (56) gives (57), including its constant.
\(\square\)

Parseval's identity also writes the first conclusion as
\(\sum_{k,\ell}4\sin^2(\pi k/N)|\widehat f_N(k,\ell)|^2
=O(N^{-1})\), and similarly for \(\ell\).
This is concentration near the trivial translation character in
that weighted sense. It does not by itself force the value at that
character to be nonzero. Equation (59) is the independent ingredient
that proves the actual coefficient lower bound.

The operators in this corollary act on the two transformed indices
of one corner-deleted vertex. They are not the crossing operator,
its cap vectors, or the final open-chain scalar. The connection to
that original scalar is the already-proved error estimate (31),
while its remaining wire-cycle analysis is still required.
