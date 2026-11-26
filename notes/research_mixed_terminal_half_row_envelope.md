# Bounding every row at the terminal half-period

Research deduction, 5 November 2026. The full absolute row envelope at
the terminal half-period can be bounded by one strictly concave
one-variable maximum and two explicit height terms. The bound includes
all upper rows, even outside the neighboring-height range where an
earlier theorem deletes them. This supplies an algebraic and variational
comparison target; its comparison with the geometric action still
requires a separate inequality.

## 1. The full envelope and the rows above one half

Use the real primitive
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt\quad(0\le u\le1),
 \qquad J(u+1)=J(u),\qquad J(1-u)=-J(u).
\]
In particular \(J(0)=J(1/2)=J(1)=0\).
Put \(b_2=-4J(1/4)=2G_{\rm Cat}/\pi\). For a complex
neighbor \(a=x+ih\) and a real row \(0\le u\le1\), define
\[
 \begin{split}
 I_a(u)&=\int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt,\\
 E_\epsilon(a,u)&=I_a(u)+J(u+1/2)-(2+\epsilon)J(u)-2\pi hu,\\
 R_\epsilon(a)&=\max_{0\le u\le1}E_\epsilon(a,u).
 \end{split}                                                   \tag{1}
\]
These are the complete raw rates at \(e=1/2\) in
[the terminal reduction](research_mixed_terminal_right_endpoint_reduction.md#4-a-joint-comparison-without-a-neighboring-height-restriction).
In the original two block types \(\epsilon=0,1\); the row
inequalities below hold for every real \(\epsilon\ge0\).
The first-target chirp is the last term in (1).

The original [whole-product arc bound](research_mixed_boundary_strip_bounds.md#2-a-product-bound-that-includes-the-whole-finite-period)
gives, for every \(a\),
\[
 I_a(u)\le -2J((1-u)/2)+2\pi h_+u,\qquad h_+=\max(h,0).
                                                               \tag{2}
\]
On the unit circle, the maximal integral over an arc of length
\(u\) is attained when that arc is centered at \(1/2\).
Inside the circle the same bound follows from subharmonicity and
the maximum principle; outside, factor out its radius in each
factor. Thus (2) retains the full complex height.

**Theorem 1.** Let \(H=\max(-h,0)\). For every
\(1/2\le u\le1\),
\[
 E_\epsilon(a,u)\le
                  \max\{2\pi H,\ b_2/2+\pi H\}.            \tag{3}
\]
No upper bound on \(|h|\), and no restriction on \(x\), is needed.

*Proof.* Put \(v=1-u\). By (2) and the two identities for \(J\),
\[
 E_\epsilon(a,u)\le B_\epsilon(v)+2\pi H(1-v),\qquad
 B_\epsilon(v)=-2J(v/2)+J(1/2-v)+(2+\epsilon)J(v).
                                                               \tag{4}
\]
For \(0<v<1/2\),
\[
 \frac{B_\epsilon''(v)}{\pi}
       =-\tfrac12\cot(\pi v/2)+\tan(\pi v)
                                  +(2+\epsilon)\cot(\pi v).
\]
Multiply this expression by the positive number
\(2\sin(\pi v)\cos(\pi v)\), and write \(c=\cos(\pi v)\).
The result is
\[
               2-c+(1+2\epsilon)c^2>0.                  \tag{5}
\]
Thus the continuous function on the right of (4) is convex on
\([0,1/2]\). Its maximum is attained at an endpoint.
Since \(B_\epsilon(0)=0\) and
\(B_\epsilon(1/2)=-2J(1/4)=b_2/2\), those two endpoint
values are exactly (3). \(\square\)

Consequently, with
\(R_\epsilon^{<}(a)=\max_{0\le u\le1/2}E_\epsilon(a,u)\),
\[
 R_\epsilon(a)\le
 \max\{R_\epsilon^{<}(a),\ 2\pi H,\ b_2/2+\pi H\}.
                                                               \tag{6}
\]
This does not assert that the upper rows are smaller than the lower
maximum. It bounds them explicitly when that stronger assertion is
unavailable.

## 2. The lower maximum has a unique scalar critical point

Suppose \(0<x<1/2\). For \(0<u<1/2\), both \(a\) and
\(a+u\) lie in the original sine strip. The exact identity
\(1-e^{-2\pi iz}=2ie^{-\pi iz}\sin\pi z\) gives
\[
 E_\epsilon(a,u)=
 \Re\{J(a+u)-J(a)\}-\pi hu
        +J(u+1/2)-(2+\epsilon)J(u).                       \tag{7}
\]
Here complex \(J\) is the continuation whose derivative is
\(\operatorname{Log}(2\sin\pi z)\). Formula (7) retains the
sign of \(h\); no absolute-height replacement has been made.

Its first and second derivatives are
\[
 \begin{split}
 E_u&=\log|2\sin\pi(a+u)|-\pi h+\log(2\cos\pi u)
                                  -(2+\epsilon)\log(2\sin\pi u),\\
 \frac{E_{uu}}{\pi}
   &=\Re\cot\pi(a+u)-\tan\pi u-(2+\epsilon)\cot\pi u
                                                      <-2.
 \end{split}                                                   \tag{8}
\]
To prove the last bound, if \(x+u\ge1/2\), the first
cotangent has nonpositive real part. The remaining terms have
sum at most \(-2\sqrt{2+\epsilon}\). If \(x+u<1/2\), use
\[
 \Re\cot\pi(a+u)\le\cot\pi(x+u)<\cot\pi u
\]
and \(\tan\pi u+(1+\epsilon)\cot\pi u\ge2\).
These inequalities hold at every finite height \(h\).

Moreover \(E_u\to+\infty\) as \(u\downarrow0\) and
\(E_u\to-\infty\) as \(u\uparrow1/2\). Therefore the lower
maximum occurs at one interior point \(u_*(a)\), and for any
trial \(v\in(0,1/2)\),
\[
 R_\epsilon^{<}(a)\le
        E_\epsilon(a,v)+\frac{E_u(a,v)^2}{4\pi}.           \tag{9}
\]
Indeed integration of (8) bounds \(E(a,u)\) by
\(E(a,v)+E_u(a,v)(u-v)-\pi(u-v)^2\); maximize this quadratic
over the real line. Formula (9) does not require an approximate
root to have been accurately solved.

For \(\epsilon=0,1\), the exact critical equation is algebraic
in a positive real variable. Set
\[
 T=\tan(\pi u_*),\quad
 A_0=|\sin\pi a|^2,\quad A_2=|\cos\pi a|^2,\quad
 B=\sin(2\pi x),\quad q_h=e^{-2\pi h}.
\]
Squaring the positive equality \(e^{E_u}=1\) gives
\[
 4^\epsilon T^{4+2\epsilon}
       =q_h(A_0+BT+A_2T^2)(1+T^2)^\epsilon.              \tag{10}
\]
All factors used in squaring are positive. Hence the unique positive
root of this quartic or sextic is exactly the unique maximum from
(8), not a different logarithmic branch. The coefficients
\(A_0,A_2,B,q_h\) are elementary functions of the neighbor.
These scalar equations describe a row majorant, not an
identification with the knot's \(A\)-polynomial.

## 3. Comparing the envelope on a complex boundary

For each fixed \(u\), \(a\mapsto I_a(u)\) is subharmonic.
One proof regularizes the logarithm as
\(\tfrac12\log(|1-e^{-2\pi i(a+t)}|^2+\delta)\), integrates
its mean inequality, then lets \(\delta\downarrow0\).
The limit is finite: the logarithmic zeros in the \(t\)-interval
are integrable. Their negative parts are uniformly integrable on
compact parameter sets, since near each simple zero they are
bounded by a constant plus \(|\log|t-t_0||\) on the real
projection. This also proves joint continuity in \((a,u)\).
The signed chirp in (1) is harmonic in \(a\).

It follows that \(R_\epsilon\) is continuous and subharmonic.
Explicitly, at the center of any parameter disk, choose a row
attaining the compact maximum in (1). Apply its mean inequality,
then bound that row by \(R_\epsilon\) on the boundary circle.
This proves the submean inequality for \(R_\epsilon\) without
assuming a differentiable maximizing row.

Let \(\Phi(a)\) be a holomorphic original critical-value function
on a neighborhood of a closed rectangle, and let \(c_0\) be real.
Then
\[
             \Re\Phi(a)-c_0-R_\epsilon(a)                \tag{11}
\]
is continuous and superharmonic. A lower bound on its rectangle
boundary therefore holds throughout the rectangle. The same
conclusion holds with \(R_\epsilon\) replaced by the explicit
majorant in (6): the lower-row maximum is subharmonic by the same
argument, \(H=\max(-\Im a,0)\) is subharmonic, and a finite maximum
of these continuous subharmonic functions is subharmonic.

This principle applies to the unchanged complex neighbor variable.
The real-linear attenuation
\(a\mapsto\Re a+i\lambda\Im a\) is generally not holomorphic
when \(\lambda\ne1\), so composing with it does not justify the
same minimum-principle argument. Nor may a real variationally
optimized value be called harmonic merely because its ingredients
come from holomorphic functions.

For the terminal source, take \(\Phi\) to be the original
optimized terminal action and \(c_0=h(1/2)\), in the notation of
[the calibrated half-point comparison](research_mixed_terminal_half_endpoint_gap.md).
A strict lower bound in (11), or for the stronger majorant (6),
would combine with
[the full right-half reduction](research_mixed_endpoint_polynomial_collar.md#4-the-joint-right-half-bound-including-its-endpoint).
The latter already includes the endpoint layer, all rows, both
parities and the actual terminal Fourier factors. The remaining
external Fourier allocation must be common to the two compared
configurations. No strict geometric lower bound for (11) on a
new parameter domain is proved in this note.

