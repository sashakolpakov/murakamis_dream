# A symmetric finite source for the original power-four vertex

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The original three-to-four convolution can be summed exactly before
separating its crossing residue from its larger endpoint contribution.
The result is a symmetric two-index finite source. All original
normalizations and both level parities are retained. This note does not
select a dominant stationary contribution from that finite sum.

## 1. The exact two-index formula

Use the original crossing matrix \(M\), reversal \(J\), cardinal
vector \(h\), scalar \(\kappa\), and notation of the
[interface proof](research_three_four_source_interface.md). Thus
\(Q=e^{2\pi i/N}\), \(r=Q^{-1}\),
\(X=e^{2\pi ix}\), \(Y=e^{2\pi iy}\), and
\[
 c_x=N^{-1}e^{-\pi i(N-1)x}(1-X^N),\qquad
 V_{4,N}(x,y)=h(x)^TJM^4h(y).
 \tag{1}
\]
All constant root-product denominators below have lengths strictly
less than \(N\), so they are nonzero.

**Theorem 1.** The full original kernel is exactly
\[
 \boxed{
 V_{4,N}(x,y)=\kappa^2 N c_xc_y
 \sum_{\substack{i,k\ge0\\i+k<N}}
 \frac{X^iY^k(r;r)_{i+k}}
 {(r;r)_i(r;r)_k(X;r)_{i+1}(Y;r)_{k+1}}.}
 \tag{2}
\]
Initially the identity is read away from the displayed moving
denominators. After multiplication by \(c_xc_y\), their poles are
removable in the entire original kernel. Consequently (2) retains
every original value and derivative, including the physical first
normals. There is no corner deletion or restriction on parity.

## 2. Exact extraction of the intermediate wire

The [exterior-source identity](research_exterior_crossing_phase.md#6-an-exact-starting-contour-for-the-full-finite-sum)
allows the original Fourier period to be taken at any fixed negative
height. Write \(Z=e^{2\pi iz}\) and \(u=Z^{-1}\), so
\(|u|<1\). Its literal three-vertex summand and crossing sum are
\[
 \begin{split}
 T_{ij}(X,Z)&=
 \frac{X^iZ^j(r;r)_{i+j}}
 {(X;r)_{i+1}(Z;r)_{j+1}}=-u A_{ij}(u),\\
 A_{ij}(u)&=
 \frac{(-1)^jQ^{j(j+1)/2}X^i(r;r)_{i+j}}
 {(X;r)_{i+1}(u;Q)_{j+1}},\\
 G_N(Z,Y)&=-u B_N(u;Y),\qquad
 B_N(u;Y)=\sum_{k=0}^{N-1}\frac{b_k(Y)Q^k}{1-uQ^k},\\
 b_k(Y)&=\frac{Y^k(r;r)_k}{(Y;r)_{k+1}}.
 \end{split}
 \tag{3}
\]
These are exact finite identities. All the functions in \(u\) on
the right are holomorphic in \(|u|<1\).

The original prefactor satisfies
\[
 c_z^2=N^{-2}u^{-N-1}(1-u^N)^2.
 \tag{4}
\]
The constant Fourier coefficient of a holomorphic function of
\(u=e^{-2\pi iz}\) is its ordinary power-series constant term.
Hence the exact convolution \(N\int V_{3,N}(x,z)C_N(z,y)\,dz\)
is
\[
 V_{4,N}(x,y)=\frac{\kappa^2c_xc_y}{N}
 \sum_{i+j<N}[u^{N-1}]A_{ij}(u)B_N(u;Y).
 \tag{5}
\]
In obtaining (5), the two nonconstant terms of \((1-u^N)^2\)
cannot contribute to the coefficient of order \(N-1\).
This is exact coefficient extraction, not a contour estimate.

Let \(P_j(u)=\prod_{a=j+1}^{N-1}(1-uQ^a)\). Since
\((u;Q)_N=1-u^N\),
\[
 \frac1{(u;Q)_{j+1}}=\frac{P_j(u)}{1-u^N}.
 \tag{6}
\]
For \(0\le k<N\), the needed coefficient is therefore
\[
 [u^{N-1}]\frac1{(u;Q)_{j+1}(1-uQ^k)}
 =
 \begin{cases}
 0,&k>j,\\[1mm]
 Q^{-k}\dfrac{(Q;Q)_{N-1-k}}{(Q;Q)_{j-k}},&k\le j.
 \end{cases}
 \tag{7}
\]
For \(k>j\), the denominator factor cancels from \(P_j\),
leaving degree below \(N-1\). Otherwise expansion of the last
geometric denominator gives
\(Q^{k(N-1)}P_j(Q^{-k})\), the second line of (7).

The root-product complement identity
\((r;r)_k(Q;Q)_{N-1-k}=N\) now gives the full triple sum
\[
 V_{4,N}(x,y)=\kappa^2c_xc_y
 \sum_{\substack{i+j<N\\0\le k\le j}}
 \frac{(-1)^jQ^{j(j+1)/2}X^iY^k(r;r)_{i+j}}
 {(X;r)_{i+1}(Y;r)_{k+1}(Q;Q)_{j-k}}.
 \tag{8}
\]
Thus the whole crossing contribution has already been combined
before any stationary approximation or absolute bound.

## 3. Finite binomial cancellation restores symmetry

Fix \(i,k\) and put \(j=k+l\),
\(d=N-1-i-k\). Conversion of the denominator in (8) gives
\[
 \frac{(-1)^jQ^{j(j+1)/2}}{(Q;Q)_{j-k}}
 =\frac{(-1)^kQ^{k(k+1)/2+kl}}{(r;r)_l}.
 \tag{9}
\]
The elementary finite binomial identity is
\[
 \sum_{l=0}^d\frac{(r^{-d};r)_l}{(r;r)_l}a^l
                          =(ar^{-d};r)_d.
 \tag{10}
\]
It follows, for example, by expanding the finite product on the
right with the usual binomial recurrence; all denominators are
nonzero for \(d<N\). In our sum
\(r^{i+k+1}=r^{-d}\), so (10) at \(a=r^{-k}\) gives
\[
 \sum_{l=0}^d\frac{(r;r)_{i+k+l}}{(r;r)_l}r^{-kl}
   =(r;r)_{i+k}(r^{i+1};r)_d
   =\frac{(r;r)_{i+k}(r;r)_{N-1-k}}{(r;r)_i}.
 \tag{11}
\]
Finally
\[
 (-1)^kQ^{k(k+1)/2}(r;r)_{N-1-k}
                                  =\frac{N}{(r;r)_k}.
 \tag{12}
\]
Substituting (9)--(12) into (8) proves (2). This all-level proof
does not use a numerical fit or an asymptotic identity. \(\square\)

## 4. The remaining finite-contour problem

On the regular index interior, the exact factorial and denominator
interpolants give the phase of the summand in (2):
\[
 F_4(s,t;x,y)=\mathcal J(s+t)-\mathcal J(s)-\mathcal J(t)
  -i\pi st+s\Log X+t\Log Y-I_X(s)-I_Y(t).
 \tag{13}
\]
The functions and logarithmic lifts are those in the
[root-product interpolation](research_root_pochhammer_interpolation.md)
and [crossing transport](research_crossing_cauchy_transport.md).
The outside prefactor in (2) contributes \(-\pi i(x+y)\)
to the action when \(|X|,|Y|<1\). If
\(U=e^{-2\pi is}\), \(V=e^{-2\pi it}\), then
\[
 e^{(F_4)_s}=\frac{X(1-UV)}{(1-U)(1-XU)},\qquad
 e^{(F_4)_t}=\frac{Y(1-UV)}{(1-V)(1-YV)}.
 \tag{14}
\]
At the validated alternating reference \(X=Y=K\), the selected
algebraic solution is
\[
       U=V=\frac{1-K}{2K}=Z_0^{-1},\qquad s=t=z_0.
 \tag{15}
\]
Both endpoint products now lie inside their original disk domains;
the factorial arguments \(s,t,s+t\) lie in their regular strips.
Thus this exact grouping removes the exterior denominator and the
moving-pole split from the finite source itself.

Equations (13)--(15) identify an analytic target. They do not yet
bound the full real index triangle, its boundary faces, or the
root-of-unity alias contours, and do not assign a nonzero coefficient
to the stationary point in the original finite sum. Those are the
remaining source estimates needed for a power-four packet and its
use in arbitrary mixed words.

Run `python3 experiments/check_power_four_finite_source.py`.
The [record](../repro/results/research-power-four-finite-source.json)
separates exact finite algebra from the unproved asymptotic claim.
