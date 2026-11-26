# The selected outer Gaussian and the remaining finite currents

Private finite-source assembly, 9 November 2026. The original outer
observation is decomposed into a nonzero local Gaussian contribution,
three explicitly retained complex currents, and the already bounded
physical tail. The local coefficient includes the exact reflected
factor, including its value two at zero cosine frequency.

This does not prove that the remaining currents are smaller. In
particular it does not yet give a nonzero asymptotic for the whole
observation. No mathematical numerical evaluation or saved-value
arithmetic is used.

## 1. The observation and the available analytic source

Use the exact conventions of
[the paired outer contour](research_mixed_next_outer_far_nodes_and_paired_contour.md).
In particular,
\[
 D=N-1,\quad M=\lceil N/2\rceil,\quad
 U=\lfloor N/2\rfloor-1,\quad \eta_N=(-1)^D,\quad
 C_{N,3}=\exp(3\pi iD^2/(4N)).
 \tag{1}
\]
The original full inner kernel and shortened-output inner kernel are
\[
\begin{aligned}
 Q_N^{\rm full}(u)
   &=\phi_N^{(x)}[R_N(x)^3K_N(-2,x)K_N(x,-2\cos u)],\\
 Q_N^{\rm sh}(u)
   &=\phi_N^{(x)}[R_N(x)^3K_N(-2,x)K_N^<(x,-2\cos u)],\\
 K_N(x,y)&=\sum_{j=0}^{D}e_j(x)e_j(y),\qquad
 K_N^<(x,y)=\sum_{j=0}^{U}e_j(x)e_j(y).
\end{aligned}
 \tag{2}
\]
Here \(\phi_N\) is the full original Hermite functional, \(R_N\) is
the original crossing, and the Newton polynomials retain their
original normalization. The ordinary spectral polynomial underlying
\(Q_N^{\rm full}\) is denoted by \(\widehat Q_N^{\rm full}\).
The observation is
\[
 {\cal O}_{N,k}
   =\phi_N[R_N^3e_M\widehat Q_N^{\rm full}T_k(-\,\cdot/2)],
 \qquad \delta=\frac12-\frac{k}{N}.
 \tag{3}
\]
The exact low-edge reduction, followed by the parity fold, licenses
the shortened source in the finite sampling formula below. No
off-grid equality of the two functions in (2) is used.

Let \(u_\delta=\beta_\delta-iK_\delta\) be the original selected
stationary point, and retain
\[
 \Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\qquad
 {\cal S}(\delta)=\Psi_\delta(u_\delta),\qquad
 \Gamma(\delta)=\Re{\cal S}(\delta).
 \tag{4}
\]
The [independent-domain theorem](research_mixed_next_independent_wedge_inner_packet.md)
gives a fixed open neighborhood \(\Omega\) of the entire selected
curve on which
\[
 A_N(u):=C_{N,3}^{-1}N^{3/2}e^{-NS(u)}Q_N^{\rm sh}(u)
             ={\cal A}(u)\{1+O_{\rm hol}(N^{-1})\}.
 \tag{5}
\]
The function \({\cal A}\) is the original nonzero Gaussian coefficient.
Every fixed derivative of the normalized error is uniformly
\(O(N^{-1})\) on fixed smaller neighborhoods.

Fix \(0<\delta_1\le1/2\), and consider all integer frequencies
in (3) with \(\delta_1\le\delta\le1/2\). Write
\[
 K_{\min}=\min_{\delta_1\le\delta\le1/2}K_\delta>0,\qquad
 \beta_{\min}=\min_{\delta_1\le\delta\le1/2}\beta_\delta>0.
 \tag{6}
\]
Choose a fixed \(r>0\) such that the closed \(2r\)-neighborhood
of this compact curve lies in \(\Omega\), and such that
\[
                 2r<K_{\min}/2,\qquad
                 2r<\beta_{\min}/2,\qquad r<1/21.
 \tag{7}
\]
All choices depend on \(\delta_1\), not on \(N,k\).

## 2. Exact finite currents

Keep the original parity amplitudes
\[
 a_N(u)=
 \begin{cases}
 \sin u,&N\text{ even},\\
 \sin u\,\sin(u/2)/\cos^2(\pi/(2N)),&N\text{ odd},
 \end{cases}
 \qquad
 \chi_N=\begin{cases}i,&N\text{ even},\\-1,&N\text{ odd}.\end{cases}
 \tag{8}
\]
Let \(T_N\) be the exact midpoint cut in equation (19) of the
paired-contour theorem. In particular
\[
 3/2\le T_N<3/2+2\pi/N,\qquad
                  \eta_Ne^{-iN(\pm T_N)}=-1.
 \tag{9}
\]
Define the entire source and complete sampling kernel by
\[
 f_{N,\delta}(u)=a_N(u)Q_N^{\rm sh}(u)
       e^{N(3iu^2/(4\pi)-i\delta u)},\qquad
 H_N(u)=\frac1{1-\eta_Ne^{-iNu}},\qquad
 P_k(u)=1+e^{-2iku}.
 \tag{10}
\]
The function \(P_k\) is the exact sum of the two reflected charges.
It is not an additional approximation.

For a piecewise smooth oriented path \(\gamma\) avoiding the real
sampling poles, put
\[
 {\cal I}_{N,k}(\gamma)
    =\frac{\chi_NC_{N,3}N}{4\pi}
          \int_\gamma H_N(u)f_{N,\delta}(u)P_k(u)\,du.
 \tag{11}
\]
Take the following four segments:
\[
\begin{aligned}
 \gamma_L &: -T_N-iK_\delta\longrightarrow u_\delta-r,\\
 \gamma_G &: u_\delta-r\longrightarrow u_\delta+r,\\
 \gamma_R &: u_\delta+r\longrightarrow T_N-iK_\delta,\\
 \gamma_V &: T_N-iK_\delta\longrightarrow T_N+iK_\delta.
\end{aligned}
 \tag{12}
\]
The first three are horizontal and oriented left to right. The
last is oriented upwards, lies on an exact midpoint line, and
therefore meets no sampling pole. Equations (1),(6),(7),(9) ensure
that these paths are well defined for all sufficiently large \(N\).

Set
\[
 G_{N,k}={\cal I}_{N,k}(\gamma_G),\quad
 L_{N,k}={\cal I}_{N,k}(\gamma_L),\quad
 R_{N,k}={\cal I}_{N,k}(\gamma_R),\quad
 V_{N,k}={\cal I}_{N,k}(\gamma_V).
 \tag{13}
\]
The original finite fold and exact paired rectangle give
\[
 \boxed{\quad
 {\cal O}_{N,k}=G_{N,k}+L_{N,k}+R_{N,k}+V_{N,k}
                                  +E_{N,k}^{\rm phys},
 \quad}
 \tag{14}
\]
where
\[
 E_{N,k}^{\rm phys}
    =\frac{\chi_NC_{N,3}}2
       \sum_{\substack{0\le j<N\\|u_j|\ge T_N}}
            a_N(u_j)Q_N^{\rm sh}(u_j)
            e^{N(3iu_j^2/(4\pi)-i\delta u_j)},\qquad
 u_j=\pi-(2j+1)\pi/N .
 \tag{15}
\]
The endpoints \(T_N\) are not nodes, so no endpoint convention
changes this partition. The physical-tail theorem proves
\[
                  |E_{N,k}^{\rm phys}|
                     \le C e^{N(\Gamma(\delta)-1/100)}.
 \tag{16}
\]
The same bound holds for the absolute sum in (15).

To obtain (14), apply the paired-contour identity at height
\(h=K_\delta\). Its bottom is exactly the first three paths
in (12), and its right side is the fourth. The identity is
valid for every positive height, and (6) keeps these heights
uniformly away from zero on the stated parameter interval.
The upper and left sides have already been included by
reflection in \(P_k\). The exact rational function \(H_N\)
still retains all sampling corrections.

## 3. A uniform nonzero local Gaussian

Put
\[
 a^{\rm par}(u)=
 \begin{cases}
 \sin u,&N\text{ even},\\
 \sin u\,\sin(u/2),&N\text{ odd}.
 \end{cases}
 \tag{17}
\]
The square root in the following statement is the one with
positive real part.

**Theorem.** Uniformly for all the integer frequencies in (6),
at both parities,
\[
 \boxed{\quad
 G_{N,k}
   =\frac{\chi_NC_{N,3}^{\,2}}{2\sqrt{2\pi}}\,N^{-1}
       \frac{a^{\rm par}(u_\delta){\cal A}(u_\delta)
                         (1+e^{-2iku_\delta})}
            {\sqrt{-\Psi_\delta''(u_\delta)}}
       e^{N{\cal S}(\delta)}\{1+O(N^{-1})\}.
 \quad}
 \tag{18}
\]
The modulus of the displayed coefficient, excluding \(N^{-1}\)
and the exponential, is bounded above and away from zero,
uniformly in \(N,k\) in this range. In particular \(G_{N,k}\ne0\)
for all sufficiently large levels.

*Proof.* By the adopted horizontal descent theorem,
\[
       \Re\Psi_\delta''(u)<-\frac1{50\pi}
 \tag{19}
\]
on the positive rectangle containing every \(\gamma_G\).
Indeed \(0<\beta_\delta\le8/7\), \(K_\delta<2/5\), and the
choice \(r<1/21\) keeps its real coordinate below \(4/3\).
At the selected point the full complex first derivative vanishes.
Consequently
\[
 \Re\Psi_\delta(u_\delta+x)
       \le\Gamma(\delta)-\frac{x^2}{100\pi}
                          \qquad (-r\le x\le r).
 \tag{20}
\]
The original analytic phase has uniformly bounded fixed
derivatives on a neighborhood of these compact segments.

Every point in their \(r\)-neighborhood has imaginary part
at most \(-K_{\min}/2\). On this set,
\[
 H_N(u)=1+O(e^{-NK_{\min}/2});
 \tag{21}
\]
each fixed derivative of the error is bounded by a fixed
power of \(N\) times that exponential. Also, for \(k\ge1\),
\[
 |e^{-2iku}|\le e^{-kK_{\min}},\qquad
 |P_k(u)|\ge1-e^{-K_{\min}}>0.
 \tag{22}
\]
For \(k=0\), \(P_0=2\). Each fixed derivative of the
nonconstant term in \(P_k\) is uniformly bounded because
\((2k)^j e^{-kK_{\min}}\) is bounded over positive integers.
These are bounds on the exact \(k\)-dependent amplitude,
not a deletion of the reflected charge.

Insert the exact normalized function (5) in (11), only on
\(\gamma_G\). Its prefactor becomes
\(\chi_NC_{N,3}^2/(4\pi\sqrt N)\), and its amplitude is
\[
                    a_N(u)A_N(u)H_N(u)P_k(u).
 \tag{23}
\]
Equations (5),(21),(22) give uniform fixed derivative bounds
for this analytic amplitude. It differs from
\(a^{\rm par}(u){\cal A}(u)P_k(u)\) by \(O(N^{-1})\),
with the corresponding normalized derivative estimates.
Here the odd factor \(\cos^{-2}(\pi/(2N))=1+O(N^{-2})\);
it is retained until this step.

For completeness, (20) bounds the portions outside a fixed
saddle neighborhood exponentially below \(\Gamma\).
Inside that neighborhood, use the real horizontal coordinate
\(x\) and expand both the analytic phase and amplitude.
After the rescaling \(x=N^{-1/2}y\), the leading integral is
\(\sqrt{2\pi}/\sqrt{-\Psi_\delta''(u_\delta)}\).
The terms of relative order \(N^{-1/2}\) are odd in \(y\)
and integrate to zero on the symmetric interval. The
remaining Taylor terms have relative integral \(O(N^{-1})\),
uniformly by (20) and the fixed derivative bounds. For example,
one may expand first on \(|x|\le N^{-2/5}\); its complement
has bound \(e^{-cN^{1/5}}\), and Gaussian moments bound the
expanded cubic, quartic, and amplitude terms on the inner
interval. This proves the uniform Gaussian formula.

The resulting scalar is
\[
       \frac{\chi_NC_{N,3}^2}{4\pi\sqrt N}
                     \sqrt{\frac{2\pi}{N}}
       =\frac{\chi_NC_{N,3}^2}{2\sqrt{2\pi}}\,N^{-1}.
 \tag{24}
\]
This proves (18). The Hessian is nonzero by (19).
The original \({\cal A}\) is nonzero; neither sine in (17)
vanishes on this compact selected curve, since its imaginary
part is strictly negative. Finally (22) proves the required
uniform lower bound for the reflected factor. Compactness
therefore bounds the complete leading coefficient away from
zero, proving nonvanishing for sufficiently large \(N\).
\(\square\)

At \(k=0\), the leading amplitude in (18) contains the exact
factor two. If \(k\) stays bounded while \(N\) grows, the
factor \(1+e^{-2iku_\delta}\) remains in the formula. It is
not replaced by one. The even-level endpoint \(\delta=0\),
where the original observation is exactly zero, is outside
the stated range.

## 4. The precise estimate still needed

Equations (14)--(18) show what would suffice to obtain the
full response on this frequency interval: a uniform positive
\(\epsilon\) for which
\[
          |L_{N,k}+R_{N,k}+V_{N,k}|
                    \le C N^B e^{N(\Gamma(\delta)-\epsilon)}.
 \tag{25}
\]
Bounds for the three absolute values separately would also
suffice. Such bounds have not been proved in this note.
The open neighborhood used in (5) does not contain the
entire negative bottom or the right connector.

The exact decomposition makes the local Gaussian a term of
the original finite observation. It does not prove that this
term survives addition of the unestimated currents. Nor would
(25), by itself, compare the complete observation after the
outgoing coefficients are attached with the geometric reference
rate \(\Lambda\). That quantitative comparison and stability
under arbitrary fixed short partial fillings remain required
for the original finite-exception target.

## Frozen source bindings

- Exact paired outer contour and physical-tail estimate:
  4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7.
- Independent-domain inner packet and normalized derivatives:
  2b306e4ba11039f88c1c1e3daad75da87223313623e37f0a34b80a81ce2a4e9e.
- Original selected curve and logarithmic charge:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Positive horizontal descent:
  c069665bd0780f72990ba55680a756d780c577c895ba4272e91af43e00c9ac7f.
- Original low-edge identity:
  76524c28bdbafafe8922993093e3e5b4447ec033e4b0dd3928295047bfde797a.
