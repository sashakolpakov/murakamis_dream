# A whole-source bound when both tapered angles are small

Research proof, 4 November 2026. The 256-bit author certificate and
fresh independent 320-bit replay pass all 32 scalar segments on 216
cells and all 64 reference products on 1,633 cells. The full written
and acceptance-code review passes. Completed artifacts are unchanged.

The reduction uses angular monotonicity on the entire row period and
height convexity at its angular maximum. It does not require a compact
conditional saddle packet near zero or a high-dimensional target cover.
All selected weights and all original finite rows remain.

## 1. Domains and statement

Let \(l=11/50\), \(L=1/10\), and \(\lambda=(L/l)^2=25/121\).
Use the actual independent reference rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                                \tag{1}
\]
For \(\eta,\epsilon\in\{0,1\}\), let \(r=(a,b)\) belong to
\(R_{3+\eta}\times R_{3+\epsilon}\). The normalized primitive,
original conditional root, allocated phase and tangent plane are
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 0&=g'(s+a)+g'(s+b)-(2+\epsilon)g'(s)+2\pi ia,\\
 \Phi(a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias\\
          &\hspace{25mm}-(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \Gamma_r(z)&=\Phi(r)+\Phi_a(r)(z_1-a)+\Phi_b(r)(z_2-b).
 \end{split}                                                  \tag{2}
\]
These are the original branches from
[the endpoint theorem](research_mixed_all_endpoint_support.md).
Their holomorphy on a neighborhood of the whole reference product is
proved before the boundary maximum principle below is used.

Both target real parts lie in \([0,L]\). Their heights and selections
are allowed independently in the following larger domains:
\[
 \begin{array}{c|c|c}
 \text{type}&\sigma&h\\ \hline
 3&0&[-.03\lambda,.02\lambda]\\
 4&0&[-.057\lambda,0]\\
 4&1&[0,.014\lambda].
 \end{array}                                                   \tag{3}
\]
In particular these domains contain every original quadratic left
taper with \(h=h_*(x/l)^2\), and every selected height
\(.014(x/l)^2\), throughout \(0\le x\le L\). Reference heights and
target heights are not identified in the enlarged estimate.

Retain \(r_N=e^{-2\pi i/N}\), \(P_j=(r_N;r_N)_j\), and
\[
 C_{\epsilon,N}(X,Y)=
   \sum_{j=0}^{N-1}
    \frac{X^{-j}(r_NX;r_N)_j(r_NY;r_N)_j}{P_j^{2+\epsilon}},
 \qquad d_N(r_N^j)=P_j^{-1},\quad \deg d_N<N.                 \tag{4}
\]

**Theorem 1.** Uniformly over (1) and (3), put
\(X=e^{-2\pi iz_1}\), \(Y=e^{-2\pi iz_2}\). For both parities
and sufficiently large \(N\),
\[
 \begin{split}
 &|C_{\epsilon,N}(X,Y)|
   |d_N(X)X^{-N\sigma_1}|^{\eta/2}
   |d_N(Y)Y^{-N\sigma_2}|^{\epsilon/2}\\
 &\hspace{15mm}\le C N^A
       \exp N\{\Re\Gamma_r(z)-1/100\}.
 \end{split}                                                  \tag{5}
\]
The stronger raw bound obtained by replacing \(C_{\epsilon,N}\)
with the sum of the absolute values of all its rows also holds.
The estimate includes \(z_1=0\) and \(z_2=0\); it is not an
asymptotic statement restricted to a compact open angle square.

The half-powers in (5) are real moduli. They are not differentiated
as holomorphic half-weights. In complete original contractions they
recombine into integer powers in the usual way. No one-small
comparison with an unrestricted other target is asserted.

## 2. Entire-period angular maximum

For \(0\le u\le1\), set
\[
 I_h(u,x)=\int_0^u\log|1-e^{2\pi h-2\pi i(x+t)}|\,dt,
 \qquad x_u=\min\{L,(1-u)/2\}.                               \tag{6}
\]
For every real height \(h\),
\[
                  \max_{0\le x\le L}I_h(u,x)=I_h(u,x_u).
 \tag{7}
\]
Indeed the derivative in \(x\) is the difference of the two endpoint
logarithms. The sign of the difference of their squared moduli is
the sign of
\[
       \cos(2\pi x)-\cos(2\pi(x+u))
                   =2\sin(\pi u)\sin(2\pi x+\pi u).
 \tag{8}
\]
For \(0<u<1\), this sign is positive before
\((1-u)/2\) and negative after it throughout \(0\le x\le L\).
The claim extends continuously through zeros and \(u=0,1\).
Thus every row, including the upper rows \(u>.8\), is covered.

At this maximizing angle, \(I_h(u,x_u)\) is convex as a function
of \(h\) on all height intervals in (3). Write
\[
 c(x,h)=\Re\cot\pi(x+ih)
       =\frac{\sin(2\pi x)}{\cosh(2\pi h)-\cos(2\pi x)}.
 \tag{9}
\]
Away from the harmless zero-height limits, differentiation gives
\[
 \partial_h^2 I_h(u,x)=\pi\{c(x,h)-c(x+u,h)\}.
 \tag{10}
\]
When \(u\le4/5\), \(x_u=L\) and \(L+u\le1-L\).
On the positive-cotangent portion \(L\le x\le1/2\), \(c(x,h)\)
decreases in \(x\), since
\[
       \cos(2\pi L)\cosh(2\pi H)<1,\qquad
                  H=.057\lambda.                            \tag{11}
\]
On the remaining portion it is nonpositive. Hence (10) is
nonnegative. When \(u\ge4/5\), the endpoints are
\(x_u\) and \(1-x_u\), so (10) equals
\(2\pi c(x_u,h)>0\) for \(u<1\).
At \(u=1\), the integral is \(2\pi h_+\), which is convex.
Continuity handles every other zero-height limit.
Adding the linear original chirp \(-2\pi hu\) preserves convexity.

Define the two endpoint heights for each target type by
\[
 {\cal H}_3=\{-.03\lambda,.02\lambda\},\qquad
 {\cal H}_4=\{-.057\lambda,.014\lambda\}.
 \tag{12}
\]
Consequently the unweighted two-factor row entropy in (5) is bounded
by the maximum of the four functions with
\(h_a\in{\cal H}_{3+\eta}\), \(h_b\in{\cal H}_{3+\epsilon}\).
The selected and unselected four-type intervals in (3) were enlarged
to their common convex hull only for this kernel bound.

## 3. Original Fourier weights and the scalar row bounds

The exact Fourier polynomial obeys
\[
 \sup_{|X|\le1}|d_N(X)|\le N^A e^{N/6}.
 \tag{13}
\]
This follows from its root-interpolation formula and
\(\max_j|P_j|^{-1}\le N^A e^{N/6}\), because
\(-J(1/6)<1/6\). The maximum principle gives the interior bound.
Since its degree is less than \(N\), Bernstein's radial inequality
also gives
\[
           |d_N(X)X^{-N}|\le N^A e^{N/6},
                               \qquad |X|\ge1.                \tag{14}
\]
Thus (13) handles every unselected four-type height in (3), and
(14) handles every selected four-type height. The true forcing
part of \(d_N\) is included; no relative factorial replacement
or cancellation at \(X=1\) is used.

Put \(J(u)=\Re g(u)\) on the real period. Equations (7)--(14) reduce
the entire allocated raw-row exponent to
\[
 S_{\eta\epsilon}(u;h_a,h_b)
 =I_{h_a}(u,x_u)+I_{h_b}(u,x_u)
       -(2+\epsilon)J(u)-2\pi h_a u+\frac{\eta+\epsilon}{12}.
 \tag{15}
\]
The scalar certificate proves the following strict bounds for all
\(0\le u\le1\) and all four height choices:
\[
 \begin{array}{c|rrrr}
 (\eta,\epsilon)&(0,0)&(0,1)&(1,0)&(1,1)\\ \hline
 S_{\eta\epsilon}&<.45&<.63&<.54&<.72 .
 \end{array}                                                   \tag{16}
\]
There are sixteen one-variable functions, split exactly at \(u=4/5\).
For evaluation on either side use
\[
 I_h(u,x)=G_{|h|}(x+u)-G_{|h|}(x)+2\pi h_+u,\quad
             G_H(t)=\Re g(t-iH).                              \tag{17}
\]
All heights in (12) are nonzero, so the smooth terms and their
derivatives are regular even at \(u=0,1\). Interior cells use a
center value and the complete second-derivative remainder.
For cells touching \(0\) or \(1\), the checker retains the exact
minimum of \(J\) on the whole row interval, using its endpoints
and any contained extrema \(1/6,5/6\). No singular derivative
bound is substituted at the row endpoints.

The finite-product upper estimate is uniform through all product
zeros: truncate the logarithm below \(-\log N\). Its total variation
is \(O(\log N)\), and its integral changes by \(O(1/N)\), uniformly
for the radii in (3). The shifted Riemann sum is therefore bounded
by its full integral plus \(O(\log N)\). The all-row sine-factorial
estimate has the same error. Summing all \(N\) rows changes only
the polynomial factor. This proves that (16) bounds the literal
finite raw sum after the actual weights (13)--(14).

## 4. Geometric planes on the enlarged target rectangles

For each fixed reference, \(\Re\Gamma_r(z)\) is affine in the four
real target coordinates. Its minimum on the product of the two
enlarged target rectangles is therefore attained at one of their
sixteen corners. At each fixed target corner, \(\Gamma_r(z)\)
is holomorphic separately in the two reference variables.
Its real minimum on the reference product reduces to the sixteen
products of reference sides.

The original logarithmic affine Newton enclosures, followed by
the exact derivative
\[
 d_r\Gamma_r(z)
        =\sum_{j,k=1}^2\Phi_{jk}(r)(z_j-r_j)\,dr_k,           \tag{18}
\]
give the following outward strict lower bounds, simultaneously
for all sixteen target corners:
\[
 \begin{array}{c|rrrr}
 (\eta,\epsilon)&(0,0)&(0,1)&(1,0)&(1,1)\\ \hline
 \Re\Gamma_r&>.54&>.65&>.65&>.735 .
 \end{array}                                                   \tag{19}
\]
There are only sixty-four two-angle reference products.
The full target rectangles are then recovered by affinity, and
the full reference products by the harmonic minimum principle.
In particular this argument does not impose an unjustified
harmonic principle after selecting a reference-dependent height.

The smallest difference between (19) and (16) is \(3/200\).
The polynomial finite-product factors and all true Fourier
weights have already been retained. The weaker uniform gap
\(1/100\) in (5) follows, proving the stated source comparison.

## Reproduction

The source acceptance is a complete scalar row cover, and the
reference acceptance is a complete two-parameter boundary cover.
Floating root centers are proposals only; original logarithmic
Newton self-maps and outward Taylor estimates decide acceptance.
The checker validates all inherited primitive/source bindings.

    python3 experiments/certify_mixed_both_low_raw_support.py --precision 256
