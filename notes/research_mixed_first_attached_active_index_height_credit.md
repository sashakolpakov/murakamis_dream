# Additional height credit for a large active ordinary index

Research deduction, 7 November 2026. On the late part of the early
taper, a large first-ordinary real index has a stronger favorable
height derivative, including the changing neighbor's incidence.
If that index is the actual maximum on its fixed contour line,
its real stationarity equation forces a quantitative amount of
negative contour height. This yields an additional same-parameter
term in the coupled derivative bound.

The stationarity premise is a real-profile maximum, not a new
complex critical point. It is not imposed on independent cut or
physical-tail profiles. No remaining regular sign is asserted.

## 1. The actual regular comparison

Use the actual first-minimum coefficients, original allocations
and following regular profile of
[the two-incidence theorem](research_mixed_first_attached_two_incidence_reduction.md).
Restrict here to
\[
 \begin{gathered}
 .15\le x\le.22,\quad x\le z\le.5,\quad
 .35\le v\le.4,\quad -.108\le\eta\le0,\\
 a=x-i\lambda_a(x-.1),\quad
 b=z-i\lambda_b(x-.1),\quad s=v+i\eta,\qquad
 0\le\lambda_b\le17/20 .
 \end{gathered}                                                \tag{1}
\]
The first coefficient is in its original own-three interval
\([-7/40,3/5]\), or in the actual attached own-four interval
\((1/6,13/20)\), with the latter's unattenuated \(m\ge3\)
scope retained.
The following ordinary index and its other targets stay fixed
and retain their independent source eligibility.

The exact coupled derivative is
\[
 \begin{split}
 \mathcal H(v,\eta)&=\Re[(1-i\lambda_a)D_a-i\lambda_bD_b],\\
 D_a&=g'(e+a)+g'(s+a)-(2+\alpha)g'(a)+2\pi is,\\
 D_b&=g'(s+b)+g'(t+b)-3g'(b)+2\pi it .
 \end{split}                                                  \tag{2}
\]
Every original chirp and both changing-neighbor incidences
are present.

## 2. A stronger derivative throughout the height interval

**Lemma 1.** On (1),
\[
 \frac{\partial\mathcal H}{\partial\eta}\le-\pi
                                      \quad(\lambda_a\ge0),
 \qquad
 \frac{\partial\mathcal H}{\partial\eta}<
                  -\frac{199\pi}{240}<-\frac{4\pi}{5}
                                      \quad(\lambda_a<0).
 \tag{3}
\]

*Proof.* The original derivative identity is
\[
 \frac1\pi\partial_\eta\mathcal H
 =-1-\Im\cot\pi(s+a)
       +\lambda_a\Re\cot\pi(s+a)
       +\lambda_b\Re\cot\pi(s+b).
 \tag{4}
\]
Here
\[
               .5\le v+x\le.62,\qquad .5\le v+z\le.9 .
 \tag{5}
\]
Both shifted real cotangents are nonpositive at every height.
If \(\lambda_a\ge0\), the height of \(s+a\) is
nonpositive, so its imaginary cotangent is nonnegative.
Every additional term after \(-1\) in (4) is therefore
nonpositive, proving the first bound.

If \(\lambda_a<0\), only the first own-three case occurs.
The first shifted real cotangent is greater than \(-1/2\),
because its largest possible modulus is
\(\tan(.12\pi)<\tan(\pi/8)=\sqrt2-1<1/2\).
Its imaginary cotangent is greater than \(-1/12\).
For the only case requiring that bound, its height is positive
and at most \(.021\). Thus its hyperbolic-sine numerator
is less than \(129/920\), using the original
\(e^{.042\pi}<23/20\) bound.
Also \(\cos(.24\pi)>7/10\), so its denominator is
greater than \(17/10\). Hence its negative imaginary
part has modulus less than
\[
                          \frac{129}{1564}<\frac1{12}.
 \tag{6}
\]
For that cosine bound, use \(.24\pi<19/25\) and
\(1-(19/25)^2/2=889/1250>7/10\).
If its height is nonpositive, the imaginary part is already
nonnegative. The real-cotangent term multiplied by
\(\lambda_a\) is at most \(7/80\).
The last term of (4) is still nonpositive.
Consequently
\[
 \partial_\eta\mathcal H/\pi
             <-1+\frac1{12}+\frac7{80}=-\frac{199}{240}.
 \tag{7}
\]
This proves (3). \(\square\)

Put \(k=1\) when \(\lambda_a\ge0\), and \(k=4/5\)
when \(\lambda_a<0\). Integration gives, on the full
height interval,
\[
                 \mathcal H(v,\eta)\ge
                          \mathcal H(v,0)+k\pi(-\eta).
 \tag{8}
\]
This is a larger favorable credit than the global height
floor used earlier. It is valid for either sign of the
fixed following index height.

## 3. What a real maximizing index forces

The adjoining own-four phase is the original
\[
                  Q_1(s;a,b)=g(s+a)+g(s+b)-3g(s)+2\pi ias .
 \tag{9}
\]
Let
\[
                         R(v)=\Re Q_{1,s}(v;a,b),
 \tag{10}
\]
keeping the actual \(a,b\) heights unchanged.
The same-target zero-index-height expression is explicitly
\[
 \begin{split}
 R(v)={}&
 \log|1-e^{2\pi\Im a-2\pi i(v+x)}|
 +\log|1-e^{2\pi\Im b-2\pi i(v+z)}|\\
 &-3\log|1-e^{-2\pi iv}|-2\pi\Im a .
 \end{split}                                                  \tag{11}
\]
The last term is the original incoming chirp. Formula (11)
does not replace either target by an independent reference.

**Lemma 2.** Suppose the index in (1) is stationary in its
real direction on the chosen fixed line:
\[
                         \Re Q_{1,s}(v+i\eta;a,b)=0 .
 \tag{12}
\]
Then
\[
                         -\eta\ge\frac{[-R(v)]_+}{4\pi}.
 \tag{13}
\]

*Proof.* For every intermediate index height, the original
second derivative has imaginary part
\[
 \Im Q_{1,ss}
  =\pi\{1+I_{s+a}+I_{s+b}-3I_s\},
                       \qquad I_u=\Im\cot\pi u .
 \tag{14}
\]
The index itself has nonpositive height, so \(I_s\ge0\).
The first shifted angular cosine is nonpositive by (5),
so \(I_{s+a}<1\), regardless of its height sign.
The second shifted height is nonpositive.
Its imaginary cotangent is less than two throughout (5).
Indeed if its angular cosine is nonpositive the bound
is already one. Otherwise its real argument is in
\((.75,.9]\), and maximizing
\[
          \frac{\sinh u}{\cosh u-c}\quad(u\ge0,\ 0<c<1)
 \tag{15}
\]
gives \(1/\sqrt{1-c^2}\).
Here \(|\sin(2\pi(v+z))|\ge\sin(\pi/5)>1/2\),
so this maximum is less than two.
Therefore
\[
                             \Im Q_{1,ss}<4\pi .
 \tag{16}
\]

Differentiating the real derivative in its height direction,
\(\partial_\eta\Re Q_{1,s}=-\Im Q_{1,ss}\).
Integrating from the stationary height to zero gives
\[
                   R(v)=-\int_\eta^0\Im Q_{1,ss}(v+iu)\,du
                                      \ge-4\pi(-\eta).
 \tag{17}
\]
Combining this with \(-\eta\ge0\) proves (13).
No sign of the integrand is required. \(\square\)

Combining (8) and (13) gives the same-parameter bound
\[
 \boxed{\quad
 \mathcal H(v,\eta)\ge
       \mathcal H(v,0)+\frac{k}{4}[-R(v)]_+ ,
                 \qquad \Re Q_{1,s}(v+i\eta)=0 .
 \quad}                                                       \tag{18}
\]
Thus a negative zero-height real derivative forces enough
negative contour height to contribute the displayed positive
term. The height and a large active real index cannot be
minimized independently in this comparison.

## 4. Exact source scope

The proved real-index concavity and the lower/upper barriers
put the fixed-line central maximum strictly inside
\((.22,.4)\). Whenever that maximum lies in the sector
\(v\ge.35\), it satisfies (12), so (18) is available
for that actual maximizing profile.
No smooth dependence of the maximizing index is needed
for this pointwise statement.

Equation (12) is only a real-profile stationarity condition.
It is not an assertion that the full complex gradient
vanishes, nor an existence statement for a moving finite
packet. It must not be assigned to a real cut, a
following-index endpoint, or a high physical-row alternative.
The formula in (11) is retained symbolically; no numerical
evaluation is part of this deduction.

The additional term in (18) changes a lower expression's
dependence on \(v\) and \(x\). Its endpoint reductions or
monotonicity must be checked anew; none is imported from
the earlier affine-credit theorem.
The complete source, actual reference marginals, middle
compensation and relative pinning fee are unchanged.
Uniform regular signs and the final calibrated boundary
comparison remain open.
