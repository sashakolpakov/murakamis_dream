# Nonzero endpoint symbol of the actual circle kernel at nonreal color

Private written proof, 14 November 2026. For each fixed signed full
twist, the specified entire ordinary-circle interpolation is nonzero
on every fixed compact set of nonreal normalized colors at all large
levels. Its leading term is an explicit endpoint symbol. This is a
statement about the actual whole coefficient, including its normal
source, rather than an individual Fresnel charge. The resulting
linear exponential action is not identified with a geometric filling
action or with the original exterior period.

No numerical evaluation, mathematical code, test, or frozen-manuscript
change is used.

## 1. The original entire interpolation

Use \(p\in\mathbb Z\setminus\{0\}\), \(N\ge2\),
\(q=e^{\pi i/N}\), \(\kappa=q^{(N-1)^2/2}\), and
\(t_k=(k+1/2)/N\), with the displayed logarithm. The exact
entire coefficient from
[the coherent Gaussian source](actual_coherent_filling_gaussian_chirp.md)
and [complex-color fusion](research_complex_color_fresnel_fusion.md) is
\[
 a_N(\zeta)=\frac{\kappa^{-p}}N\sum_{k=0}^{N-1}
 [1-\zeta/N+2p(t_k-1/2)]
 e^{2\pi ipN(t_k-1/2)^2-2\pi i\zeta t_k}.
 \tag{1}
\]
At physical \(0\le n<N\) this equals the canonical first-kind
coefficient \(a_n\) of \(r_N^{2p}\) in the full pair algebra.
The specified entire ordinary-circle function is
\[
 b_N(\zeta)=e^{\pi i(\zeta-1)}
                         [a_N(\zeta-1)-a_N(\zeta+1)].
 \tag{2}
\]
For physical integer color \(1\le j<N\), this is the original
\(\beta_{j-1}\). At \(j=N\), the original last coefficient
is \(\beta_{N-1}=b_N(N)/2\), as required by its zero endpoint
convention. We do not alter that convention. The original twist
operator also retains the unit scalar \(\kappa^{2p}\).

Define holomorphic functions on the nonreal half-planes by
\[
 g_+(\beta)=\frac{p+1-\beta}{\sin(\pi\beta)},\qquad
 g_-(\beta)=\frac{p+\beta-1}{\sin(\pi\beta)}.
 \tag{3}
\]
Neither denominator vanishes there. All estimates below are uniform
on any fixed compact subset \(K\) of the indicated open half-plane;
constants may depend on \(p,K\).

## 2. The actual midpoint sum has a uniform endpoint expansion

**Lemma 1.** For \(\operatorname{Im}\beta>0\),
\[
 a_N(N\beta)=\frac{iq^{-p/2}}{2N}e^{-2\pi iN\beta}
                         [g_+(\beta)+O_{p,K}(N^{-1})].
 \tag{4}
\]
For \(\operatorname{Im}\beta<0\),
\[
 a_N(N\beta)=\frac{iq^{-p/2}}{2N}
                         [g_-(\beta)+O_{p,K}(N^{-1})].
 \tag{5}
\]
After the displayed common factors are removed, the error is
holomorphic and its derivatives of any fixed order are
\(O_{p,K}(N^{-1})\).

*Proof.* In the upper half-plane write
\(k=N-1-\ell\), \(s=\ell+1/2\). Then
\(t_k=1-s/N\), and (1) is exactly
\[
 \frac{\kappa^{-p}}N e^{\pi ipN/2-2\pi iN\beta}
 \sum_{\ell=0}^{N-1}
 [p+1-\beta-2ps/N]
             e^{2\pi i(\beta-p)s}e^{2\pi ips^2/N}.
 \tag{6}
\]
The modulus of \(e^{2\pi i\beta s}\) decays geometrically,
uniformly on \(K\). For real \(s\),
\(|e^{2\pi ips^2/N}-1|\le2\pi h s^2/N\), where
\(h=|p|\). Summing these errors and the amplitude correction
against that fixed geometric decay costs \(O(N^{-1})\).
Extending the leading sum to infinity has exponentially small
error. Its exact value is
\[
 \sum_{\ell\ge0}e^{2\pi i(\beta-p)(\ell+1/2)}
                  =\frac{i(-1)^p}{2\sin(\pi\beta)}.
 \tag{7}
\]
Finally
\((-1)^p\kappa^{-p}e^{\pi ipN/2}=q^{-p/2}\).
This proves (4), with the original phase retained.

In the lower half-plane set \(k=\ell\), \(s=\ell+1/2\),
so \(t_k=s/N\). The exact sum becomes
\[
 \frac{\kappa^{-p}}N e^{\pi ipN/2}
 \sum_{\ell=0}^{N-1}[1-\beta-p+2ps/N]
              e^{-2\pi i(p+\beta)s}e^{2\pi ips^2/N}.
 \tag{8}
\]
Its convergent leading geometric sum is
\(-i(-1)^p/(2\sin(\pi\beta))\). The same estimates give
(5). The normalized errors are holomorphic on their half-planes.
Applying the already proved bounds on a slightly larger compact
set and then Cauchy's formula gives all fixed derivative bounds.
\(\square\)

Both leading functions in (3) are nonzero at nonreal \(\beta\).
Thus the actual entire first-kind coefficient is nonzero on \(K\)
for all large \(N\). No residue-class or coprimality restriction
enters this endpoint argument.

## 3. The prescribed circle difference has a nonzero leading symbol

**Theorem 2.** The actual function (2) satisfies
\[
 \boxed{\quad
 b_N(N\beta)=\frac{iq^{-p/2}}{N^2}e^{-\pi iN\beta}
                 [g_+'(\beta)+O_{p,K}(N^{-1})],
       \qquad \operatorname{Im}\beta>0,\quad}
 \tag{9}
\]
and
\[
 \boxed{\quad
 b_N(N\beta)=\frac{iq^{-p/2}}{N^2}e^{\pi iN\beta}
                 [g_-'(\beta)+O_{p,K}(N^{-1})],
       \qquad \operatorname{Im}\beta<0.\quad}
 \tag{10}
\]
The functions \(g_+'\) and \(g_-'\) have no nonreal zero.
Consequently there are positive constants \(c_{p,K},C_{p,K}\)
such that for all sufficiently large \(N\),
\[
 \boxed{\quad
 c_{p,K}N^{-2}e^{\pi N|\operatorname{Im}\beta|}
 \le |b_N(N\beta)|
 \le C_{p,K}N^{-2}e^{\pi N|\operatorname{Im}\beta|},
                       \qquad \beta\in K.\quad}
 \tag{11}
\]

*Proof of the expansion.* Let \(F_{+,N}\) be the normalized
bracket in (4). Then
\(F_{+,N}=g_++O(N^{-1})\), including its first several
derivatives, on a neighborhood of \(K\). In the actual shifts
\(\zeta\mapsto\zeta\pm1\), the upper common exponential is
unchanged because \(e^{\pm2\pi i}=1\). Hence
\[
 F_{+,N}(\beta-1/N)-F_{+,N}(\beta+1/N)
                   =-2g_+'(\beta)/N+O(N^{-2}).
\]
Insert this into (2) and retain
\(e^{\pi i(N\beta-1)}=-e^{\pi iN\beta}\); this gives
(9). The same calculation with (5) gives (10). The derivative
control matters: subtracting two unspecified \(O(N^{-1})\)
errors alone would not justify the displayed leading difference.

*Proof of nonvanishing.* In the upper case put
\(z=\pi(\beta-p-1)\); in the lower case put
\(z=\pi(\beta+p-1)\). The integer shifts preserve cotangent.
Differentiating (3) shows that a zero of either derivative at
nonreal \(\beta\) would imply
\[
                              \sin z-z\cos z=0.
 \tag{12}
\]
There is no nonreal solution of (12). Indeed, if it held, the
nonzero function \(u(x)=\sin(zx)\) on \([0,1]\) would obey
\(-u''=z^2u\), \(u(0)=0\), and \(u'(1)=u(1)\).
Integration against \(\overline u\) gives
\[
 z^2\int_0^1|u|^2dx
      =\int_0^1|u'|^2dx-|u(1)|^2\ge0.
 \tag{13}
\]
The inequality follows from
\(u(1)=\int_0^1u'(x)dx\) and Cauchy--Schwarz. Thus \(z^2\)
is real and nonnegative, forcing \(z\) real. This contradicts
\(\operatorname{Im}\beta\ne0\).

The derivative symbols are therefore bounded above and away from
zero on \(K\). Taking moduli in (9) and (10) proves (11).
\(\square\)

## 4. What this proves and what it does not

The coefficient in (11) is the specified entire interpolation of
the whole original circle difference. Every finite Gaussian branch,
its normal source, and its endpoint current are already combined
in the midpoint formula (1). The result is therefore stronger than
nonvanishing of one retained charge integral.

The symbol proved here belongs to the endpoint contribution. Its
exponential rate is \(\pi|\operatorname{Im}\beta|\), and its
phase is linear in the continued color at leading order. It is
not the quadratic geometric surgery action of an individually
labeled Gaussian saddle. The theorem does not show that such a
saddle survives, or that the original exterior contraction keeps
this coefficient without further cancellation.

Likewise, the estimates are not uniform as
\(\operatorname{Im}\beta\to0\). They do not remove the exact
physical central zeros or the real-color resonance issues in
[the actual-circle bulk calculation](research_fused_twist_circle_coefficients.md).
They supply a source-specific nonzero endpoint symbol at fixed
nonreal color, with the entire interpolation and all phases fixed.

## Direct source versions

- `actual_coherent_filling_gaussian_chirp.md`:
  `d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522`.
- `research_complex_color_fresnel_fusion.md`:
  `002f6e8170760ec084a7cafb43da00eb936b2da7ecc05310560cbfa658438693`.
The entire circle convention in (2), including the final half
weight, is the coherent Gaussian note's equations (12d)--(12f).
