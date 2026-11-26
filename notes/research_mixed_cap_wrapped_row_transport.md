# A decreasing bound for every wrapped physical cap row

Research deduction, 7 November 2026. On the real incoming arc
\(1/2\le a\le7/10\), the entire wrapped private-row sector of the
original cap has rate at most \(h(1-a)\). This improves its former
constant ceiling and keeps the whole coherent endpoint coefficient
in each row. It does not assert that this rate is below the cap's
own continued critical action.

No numerical evaluation, saved replay or frozen-note edit is used.

## 1. Exact source and inherited real profiles

Keep the original cap
\[
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
                 H_N(w,r^{-j})\frac{p_j(X)}{P_j},\qquad
 r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j.
 \tag{1}
\]
Let \(a=1-v\), \(3/10\le v\le1/2\), \(X=e^{-2\pi ia}\).
The wrapped sector means exactly
\[
 W_N(a,w)=
 \sum_{\substack{0\le j<N\\j/N\ge v}}
                 H_N(w,r^{-j})\frac{p_j(X)}{P_j}.
 \tag{2}
\]
All original endpoint polynomials remain complete. No partial
Newton sum or separately bounded endpoint summand replaces \(H_N\).

Use the real profiles
\[
 h(e)=\Re S(e)+J(e),\qquad
 B_v(e)=J(e-v)+J(v)-J(e),\qquad b_0=101/125.
 \tag{3}
\]
Here \(J\) is the continuous one-periodic real primitive of
\(\log(2|\sin\pi e|)\), with \(J(0)=0\), and \(S\) has its original
normalization. The full-source statements in
[the wrapped-private theorem, Section 2](research_mixed_next_wrapped_private_sector.md)
give the compact-row rate \(h(e)+B_v(e)\), uniformly at every
real ordinary color \(-2\le w\le2\). Their finite product bound
is zero-safe through the incoming wall and both level parities.
The true private ends have the separate positive-source rate \(3/5\)
on \(|X|\le1\). These bounds also hold near complete ordinary
color with an arbitrarily small prescribed extra tolerance.

The original reflection and curvature identities are
\[
 \begin{gathered}
 h(1-e)=h(e),\qquad h'(1/2)=0,\\
 -h''(e)=\frac{2\pi}{\sin\pi e}
              \Re\frac1{\sqrt{\,2-e^{-2\pi ie}\,}}>18/5
                 \qquad(0<e<1/2),\\
 h(e)\le b_0-\frac95(1/2-e)^2\qquad(0\le e\le1/2).
 \end{gathered}
 \tag{4}
\]
They are proved with the original branch in
[the endpoint collar, equation (13)](research_mixed_endpoint_polynomial_collar.md)
and [the coherent far-arc proof, Section 2](research_mixed_next_coherent_cap_far_arc.md).
In particular \(h\) increases on \([0,1/2]\).

## 2. The lower wrapped half is strictly decreasing

**Lemma.** For \(3/10\le v<1/2\), the function
\(h(e)+B_v(e)\) strictly decreases on \(v<e\le1/2\).
Consequently
\[
                    h(e)+B_v(e)\le h(v)
                         \qquad(v\le e\le1/2).
 \tag{5}
\]

*Proof.* For \(3/10\le s\le1/2\),
\[
 \Re(2-e^{-2\pi is})>9/4,\qquad
 \Re(2-e^{-2\pi is})^{-1/2}<2/3.
 \tag{6}
\]
Indeed \(\cos(2\pi s)\le\cos(3\pi/5)=(1-\sqrt5)/4<-1/4\);
the modulus of the square root therefore exceeds \(3/2\).
Integrating (4) to \(1/2\) gives
\[
 h'(e)\le\frac{4\pi}{3}\int_e^{1/2}\frac{ds}{\sin\pi s}
       =\frac43\log\cot(\pi e/2)
       \le\frac43\cot\pi e.
 \tag{7}
\]
The first inequality is strict for \(e<1/2\). The last inequality is
\(\operatorname{artanh}c\le c/\sqrt{1-c^2}\) for
\(c=\cos\pi e\), obtained by comparing derivatives from \(c=0\).

For \(v<e\le1/2\),
\[
 B_v'(e)=
 \log\frac{\sin\pi(e-v)}{\sin\pi e}
 =\log\{\cos\pi v-\sin\pi v\cot\pi e\}.
 \tag{8}
\]
Its argument is positive. From \(-\log(1-z)\ge z\),
\[
 -B_v'(e)\ge-\log\cos\pi v+\tan\pi v\cot\pi e.
 \tag{9}
\]
Now \(\tan\pi v\ge\tan(3\pi/10)>4/3\).
For an exact witness, use
\(\tan^2(3\pi/10)=1/(5-2\sqrt5)>16/9\), which follows from
\(\sqrt5>71/32\). Equations (7)--(9) imply
\(h'(e)+B_v'(e)<0\), including \(e=1/2\).
Continuity at \(e=v\), where \(B_v(v)=0\), proves (5).
For \(v=1/2\), (5) is the single endpoint identity.
\(\square\)

## 3. Reflection pays the whole upper half as well

For every \(v\in[3/10,1/2]\), the already proved quotient sign is
\[
                         B_v(e)\le0\qquad(v\le e\le1).
 \tag{10}
\]
Let \(e\ge1/2\), \(f=1-e\). If \(f\le v\), reflection and
monotonicity of \(h\), together with (10), give
\(h(e)+B_v(e)\le h(f)\le h(v)\).
If \(v\le f\le1/2\), use instead
\[
 B_v(1-f)-B_v(f)
             =2J(f)-J(f+v)-J(f-v).
 \tag{11}
\]
For \(v<f<1/2\) its derivative is
\[
 \log\frac{\sin^2\pi f}
               {\sin^2\pi f-\sin^2\pi v}>0.
 \tag{12}
\]
The denominator is positive on this interval, and (11) is zero
at \(f=1/2\), by \(J(1/2+v)=-J(1/2-v)\).
Thus (11) is nonpositive throughout, including its continuous
endpoint. The lemma now gives
\[
 h(e)+B_v(e)
 =h(f)+B_v(1-f)\le h(f)+B_v(f)\le h(v).
 \tag{13}
\]
For \(v=1/2\), the first case already covers the entire upper half.
Combining (5) and (13) proves the complete real-profile inequality
\[
                 \boxed{\quad h(e)+B_v(e)\le h(v)
                       \quad(v\le e\le1).\quad}
 \tag{14}
\]

## 4. The literal finite sector, true ends and derivatives

The separate true-end rate \(3/5\) is also below \(h(v)\).
To check this without an endpoint extrapolation, the already
printed scalar consequences and curvature in
[the bridge phase floor, Section 4](research_mixed_endpoint_bridge_phase_floor.md)
give
\[
 \lambda(3/10)>
 \frac{108}{125}-\frac1{200}\frac1{20}
                    -\frac{11}{2}\left(\frac1{20}\right)^2
 =\frac{17}{20}.
 \tag{15}
\]
No saved value is recomputed here. Since \(J(3/10)>-1/6\),
\[
                  h(v)\ge h(3/10)>41/60>3/5.
 \tag{16}
\]
The wrapped index set is already separated from the lower true
endpoint by \(v\ge3/10\). For its upper true endpoint use the
original \(3/5\) positive bound. On the remaining compact index
range use the complete coherent \(H_N\) bound, (14), and the
zero-safe finite numerator and factorial estimates. Summing
at most \(N\) rows changes only a polynomial factor.

**Theorem.** For every \(\tau>0\), uniformly for
\(1/2\le a\le7/10\) and \(-2\le w\le2\),
\[
 \begin{split}
 \sum_{j/N\ge1-a}
 \left|H_N(w,r^{-j})\,p_j(e^{-2\pi ia})/P_j\right|
 &\le C_\tau N^{B_\tau}
                    e^{N\{h(1-a)+\tau\}}\\
 &\le C_\tau N^{B_\tau}
 e^{N\{101/125-(9/5)(a-1/2)^2+\tau\}}.
 \end{split}
 \tag{17}
\]
Both level parities, the wall row when present, all revived
numerator values, and the original source normalization are
included. The bound concerns a sum of the moduli of complete
coherent private rows; it is not obtained by dividing a signed
cap estimate.

Fixed ordinary-color derivatives have the same rate with polynomial
cost, by the whole-real-interval polynomial bound and Markov.
For each tolerance, the original compact source and true-end
estimates preserve (17) on a small fixed ordinary-color disk about
\(-2\). At a base incoming value, keep the integer row set in (2)
fixed. The zero-safe integrated rates and strict true-end reserve
preserve its bound with a further prescribed allowance on a small
fixed complex incoming neighborhood. Cauchy's formula then gives
all fixed outside-parameter derivatives there. No differentiation
of the moving cutoff is claimed.

The theorem is an actual improvement for the complete wrapped
physical sector. It does not compare \(h(1-a)\) with
\(\Re\mathcal T(a,-2)\), pay the retained outer cap currents,
or establish a whole-cap relative asymptotic.
