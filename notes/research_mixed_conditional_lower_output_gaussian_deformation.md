# Deforming the lower-output conditional source with two error bounds

Research deduction, 8 November 2026. The real middle integral
in [the complete source reduction](research_mixed_conditional_lower_output_middle_reduction.md)
can be moved through the actual conditional critical point,
with both unweighted connecting sides retained. Its local
Gaussian has the original nonzero coefficient. The remaining
complete source is controlled by the sum of an exponentially
smaller conditional-action term and an error already paid
against the actual ordinary-next source plane.

These are two distinct bounds. No relative asymptotic for the
whole conditional polynomial, or final comparison of its
critical action with the following plane, is asserted.
No numerical evaluation or frozen-source edit is used.

## 1. Exact source and proved critical strip

Use the parameters, cuts, interpolant and original phase from
the source reduction:
\[
 \begin{gathered}
 a=x-i\eta,\quad x\in[1/2,7/10],\quad0\le\eta\le9/125,\\
 y=z-i\xi,\quad z\in[.22,.45],\quad0\le\xi\le27/250,\\
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 s_*=u_*+ih_*,\quad \Theta(a,y)=Q(s_*;a,y),\\
 L_N=\lfloor2N/25\rfloor+1,\quad M_N=\lceil N/2\rceil,\quad
 \ell_N=(L_N-\tfrac12)/N,\quad b_N=(M_N-\tfrac12)/N.
 \end{gathered}                                                 \tag{1}
\]
The symbol \(h_*\) in this note is the conditional private
height. It is distinct from the outgoing height \(-\xi\).
The complete original source is
\[
 C_{1,N}(X,Y)=
       N\int_{\ell_N}^{b_N}T_N(s;a,y)\,ds+\mathcal E_N,
                                                               \tag{2}
\]
where all physical end rows and all six weighted cotangent
currents in \(\mathcal E_N\) have the actual ordinary-next
bound proved in that reduction.

Its Section 5 proves, on the original zero logarithmic lift,
\[
 \frac2{25}<u_*<1-x,\qquad
       \frac15<|e^{2\pi is_*}|<2,\qquad
             |h_*|<\frac{\log5}{2\pi}.
                                                               \tag{3}
\]
The critical point is simple. The original phase has strict
horizontal concavity throughout
\[
 \frac2{25}\le\Re s<1-x,\qquad
                  |\Im s|\le\frac{\log5}{2\pi}.
                                                               \tag{4}
\]
The parameter set (1) is compact; therefore the strict
critical-point separations in (3) are uniform. In particular
\(\ell_N<u_*<b_N\) for all sufficiently large \(N\).
The small displacement of \(\ell_N\) to the left of \(2/25\),
when it occurs, stays in a fixed extension of (4):
at the compact line \(\Re s=2/25\) the curvature has a
uniform strict sign, so continuity supplies that extension.

Let \(\widehat R(t,\sigma)\) be the exact continuous two-branch
upper rate of the source reduction. It equals \(\Re Q\)
before the incoming numerator wall. After that wall it keeps
both terms of the original cyclotomic identity. Its horizontal
derivative has the same modulus formula on both branches,
because their difference \(2\pi(\sigma-\eta)_+\) is independent
of \(t\).

## 2. Horizontal decrease beyond the wall at negative height

Put \(U=e^{2\pi\sigma}\), \(T=e^{2\pi\eta}\), and \(R=|Y|\).
The exact chirp-folded horizontal force is
\[
 e^{2\partial_t\widehat R}=
 \frac{|T-Ue^{-2\pi i(x+t)}|^2
       |1-RUe^{-2\pi i(z+t)}|^2}
      {|1-Ue^{-2\pi it}|^6}.
                                                               \tag{5}
\]
On the actual critical-height line, \(U>1/2\) by (3).
For nonnegative height, \(U\ge1\), the complete postwall
decrease is the polynomial inequality in
[the half-cut proof, Section 3](research_mixed_conditional_half_cut_below_incoming_zero.md).
Its outgoing bound uses \(R<8/7\), so it applies in particular
to \(R\le1\). Both exact rate branches remain included.

Here is the missing negative-height verification. Suppose
\(1/2\le U\le1\) and \(1-x\le t\le1/2\).
For \(3/10\le t\le2/5\), one has
\[
 1\le x+t\le11/10,\qquad
 \cos(2\pi(x+t))>4/5,\qquad
                         \cos(2\pi t)<-3/10 .
 \]
Convexity in \(T\in[1,8/5]\) bounds the first numerator
square by its larger endpoint bound
\(U^2-64U/25+64/25\). The endpoint at \(8/5\)
is larger than the one at one because their difference
is \(39/25-24U/25>0\). The outgoing modulus is at most
\(1+U\). Hence
\[
 e^{2\partial_t\widehat R}\le
 \frac{(U^2-64U/25+64/25)(1+U)^2}
      {(U^2+3U/5+1)^3}<1 .
                                                               \tag{6}
\]
The denominator minus numerator is exactly
\[
 P(U)=U^6+\frac95U^5+\frac{77}{25}U^4
       +\frac{547}{125}U^3+\frac{141}{25}U^2
       -\frac{19}{25}U-\frac{39}{25}.
 \]
It satisfies \(P(1/2)=2251/8000>0\) and \(P'(U)>0\)
for \(U\ge1/2\): its quadratic and linear terms already
give derivative \((282U-19)/25>0\), and all higher
derivative terms are positive.

For \(2/5\le t\le1/2\), the incoming angle lies in
\([1,6/5]\), so its cosine is positive. The own cosine
is less than \(-4/5\). It follows that
\[
 e^{2\partial_t\widehat R}\le
 \frac{(U^2+64/25)(1+U)^2}
      {(U^2+8U/5+1)^3}<1 .
                                                               \tag{7}
\]
Here the exact difference is
\[
 U^6+\frac{24}{5}U^5+\frac{242}{25}U^4
       +\frac{1462}{125}U^3+\frac{178}{25}U^2
       -\frac8{25}U-\frac{39}{25}.
 \]
Its last three terms have value \(3/50\) at \(U=1/2\)
and increase thereafter. Every higher term is positive.
The elementary cosine bounds used in (6)--(7) follow from
\(\cos(\pi/5)>4/5\) and
\(\cos(2\pi/5)>3/10\), using \(\sqrt5>11/5\).

Thus the entire postwall part of the critical-height line
strictly decreases, for either sign of \(h_*\). At a possible
incoming numerator zero the rate is continuous; integrate the
one-sided inequalities rather than asserting a differentiable
symbol there. The full finite interpolant remains holomorphic.

Together with (3)--(4), this proves that the main line from
\(\ell_N+ih_*\) to \(b_N+ih_*\) has its unique maximum
at the original \(s_*\), with value
\[
                              M=\Re\Theta(a,y).
                                                               \tag{8}
\]
Outside any fixed sufficiently small regular critical chart,
there is a uniform strict loss \(\gamma>0\), by compactness
and the proved prewall and postwall comparisons. This is an
estimate for the original continuous upper rate; no physical
wall row or cyclotomic alternative has been discarded.

## 3. Both unweighted connecting sides

The original finite integrand is holomorphic in the full
rectangle between the real line and height \(h_*\). Hence
\[
 \begin{split}
 N\int_{\ell_N}^{b_N}T_N(s)\,ds
   ={}&N\int_{\ell_N}^{\ell_N+ih_*}T_N(s)\,ds\\
     &+N\int_{\ell_N+ih_*}^{b_N+ih_*}T_N(s)\,ds
       +N\int_{b_N+ih_*}^{b_N}T_N(s)\,ds .
 \end{split}                                                    \tag{9}
\]
All orientations and the original positive factor \(N\) are
explicit. This is not an omission of the real endpoints.

On the lower connecting side, (4) and holomorphy imply
vertical convexity:
\[
 \partial_\sigma^2\Re Q(\ell_N+i\sigma;a,y)
                     =-\Re Q_{ss}(\ell_N+i\sigma;a,y)>0 .
 \]
It follows that its rate is bounded by the larger of
its two endpoint rates. The real endpoint has the actual
next-source gap of the low-block theorem. Its main endpoint
has rate at most \(M-\gamma\) by Section 2.

For the upper side, work first at the limiting half cut.
The complete two-branch rate satisfies
\[
 \begin{split}
 \partial_\sigma\widehat R(1/2,\sigma)
       &\le-2\pi(x-z)\le-\pi/10,
                                      &&\sigma<\eta,\\
 \partial_\sigma\widehat R(1/2,\sigma)
       &\ge0,                         &&\sigma>\eta .
 \end{split}                                                    \tag{10}
\]
These are the exact argument bounds from
[complete nonnegative-height continuation, Section 4](research_mixed_conditional_nonnegative_height_complete_source.md),
now with their scope made explicit. Below \(\eta\), the
incoming argument after the period shift is nonnegative,
the own argument is zero, and the outgoing argument is
at least \(-2\pi z\), at every outgoing height. Above
\(\eta\), the incoming argument is at most
\(\pi-2\pi(x-1/2)\), the outgoing argument is nonpositive,
and the second cyclotomic branch supplies \(+2\pi\).
These bounds also hold for negative \(\sigma\).

Therefore the rate along the interval joining \(0\) and
\(h_*\) is at most the larger endpoint rate. If \(h_*<0\),
it is simply maximal at \(h_*\). At the actual cut
\(b_N=1/2+O(N^{-1})\), uniform continuity of the exact
two-branch rate gives the same bound with an arbitrarily
small debit. This includes the even approaching cut and
the odd cut at one half, without differentiating a kink.
The real endpoint has the upper-block next-source gap;
the main endpoint is below \(M-\gamma\), after shrinking
\(\gamma\) if necessary.

Consequently each complete unweighted side is bounded
by the sum of an \(e^{N(M-\gamma)}\) term and its real-cut
term, with polynomial factors. Multiplying the latter
by the actual complete cap, Fourier weight and next kernel
gives the already proved following-plane gap. This argument
does not require either real cut to lie below \(M\).

## 4. Original Gaussian and the complete-source conclusion

Inside the critical chart every argument stays in its
original regular strip. The canonical factorial expansion is
\[
 \begin{split}
 T_N(s)&=N^{-3/2}b(s;a,y)e^{NQ(s;a,y)}
                              (1+O_{\rm hol}(N^{-1})),\\
 b(s;a,y)&=\frac{a_0(a+s)a_0(y+s)}
                     {a_0(s)^3a_0(a)a_0(y)},\qquad
 a_0(q)=\sqrt{2\sin\pi q}\,e^{-i\pi q/2}.
 \end{split}                                                    \tag{11}
\]
The square roots and additive phase constant are the original
ones. Strict horizontal concavity fixes the accretive Gaussian
square root. The leading coefficient is
\[
 \mathcal B(a,y)=
       \frac{\sqrt{2\pi}\,b(s_*;a,y)}
                      {\sqrt{-Q_{ss}(s_*;a,y)}}\ne0 .
                                                               \tag{12}
\]
On each fixed local parameter chart choose the usual analytic
critical contour and keep its small Morse-coordinate endpoints
fixed. Its actual local contribution \(G_N\) is holomorphic and
satisfies
\[
                  G_N(a,y)=N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                                 (1+O_{\rm hol}(N^{-1})).
                                                               \tag{13}
\]
The powers are exactly \(N^{-3/2}\cdot N\cdot N^{-1/2}=N^{-1}\).
Small contour adjustments joining this local chart to (9)
stay in the region with the strict main loss. A finite compact
cover makes all constants uniform; no full-width source
neighborhood is inferred from a local packet.

For the actual ordinary-next reference family, put
\[
 W_N=U_{0,N}(w,X)d_N(Y)C_{\beta,N}(Y,Z),\qquad
 \beta\in\{0,1\},
 \]
and retain \(\Lambda_{123}(z_{\rm out})\) and
\(|d_N(Z)|^{\beta/2}\) exactly as in the source reduction.
Equations (2), (9), and Sections 2--3 give constants
\(\gamma,\kappa>0\), independent of the compact reference,
such that
\[
 \begin{split}
 &|W_N\{C_{1,N}(X,Y)-G_N(a,y)\}|\,
                                      |d_N(Z)|^{\beta/2}\\
 &\quad\le C N^A
      |W_N|\,|d_N(Z)|^{\beta/2}
                          e^{N(\Re\Theta-\gamma)}
       +C N^A e^{N\{\Lambda_{123}(z_{\rm out})-\kappa\}} .
 \end{split}                                                    \tag{14}
\]
For example the second gap may be taken as \(1/1000\)
after sharing the proved end/current reserves and compact
continuity debits. The first term is the conditional-action
error from the main tails and main ends of the connectors.
The second is the complete next-source error from the physical
ends, weighted currents and real ends of those same connectors.
Both are bounds for the whole original finite source.

Equivalently, replacing \(G_N\) in (14) by the leading
term in (13) adds at most
\[
          C N^{-2}|W_N|\,|d_N(Z)|^{\beta/2}e^{N\Re\Theta}.
                                                               \tag{15}
\]
This displays precisely what remains to be compared with
the original following action: the actual product
\(W_N e^{N\Theta}\), with its cap and all outside factors.

The all-real ordinary-color bounds, both parities and every
original Fourier forcing alternative are retained. The outside
measures remain \(N\,da\) and \(N\,dy\). On fixed local
parameter charts the exact source, local Gaussian and
connecting integrals are holomorphic. Holding all nonlocal
paths and integer cuts fixed, the strict upper bounds persist
on smaller complex neighborhoods. Cauchy estimates give fixed-jet
bounds in the corresponding local sup norms, after reducing
\(\gamma,\kappa\) if necessary. The first bound uses the
local norm of the holomorphic product \(W_Ne^{N\Theta}\);
it is not a pointwise division by \(W_N\) at its possible zeros.
At the actual output, the usual nonzero
factorial packet removes the outgoing halfweight only there.

The two terms in (14) must not be replaced by a single error
relative to \(e^{N\Theta}\) without a new comparison. The
present theorem neither proves the needed following-plane
bound for \(W_N e^{N\Theta}\) nor estimates the remaining
outside-\(P\) part of the lower period. It is an ordinary-next
finite-source result, not a terminal-family or whole-transfer
asymptotic.
