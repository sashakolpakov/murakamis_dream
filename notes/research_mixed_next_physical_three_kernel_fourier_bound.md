# A complete Fourier bound for the physical-node three-kernel

Private written source estimate, 8 November 2026. No mathematical
numerical evaluation or change to a frozen input is used.

The complete derivative trace improves the direct absolute-trace
rate \(4b_2\). The improvement concerns the original single-three
kernel, and then the actual high-Newton coefficients. It does not
estimate their remaining outgoing \(C_0\) observation.

## 1. Source and statement

Keep the original objects and normalization of
[the direct physical trace](research_mixed_next_physical_three_kernel_absolute_trace.md),
equations (1), (13), and (17):
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad \eta=(-1)^D,\quad
 \kappa=q^{D^2/2},\\
 S_k=\prod_{a=1}^k2\sin(\pi a/N),\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 e_k(z)=S_k^{-2}\prod_{a<k}(c_a-z),\\
 K_N(w,t)=\sum_{k=0}^D e_k(w)e_k(t),\\
 \mathcal K_{3,N}(w,c_j)
 =\phi_N^{(t)}[\mathcal R_N(t)^3K_N(w,t)K_N(c_j,t)].
\end{gathered}                                                     \tag{1}
\]
The trace in (1) retains every physical value and first normal.
There is no replacement by the distinct-node trace.

**Theorem.** There are constants \(C,A\), independent of both level
parities, the real ordinary color, and the physical index, such that
\[
 \boxed{\quad
 |\mathcal K_{3,N}(w,c_j)|
 \le CN^A\exp N\left(\frac{419}{200}-\frac1{125}\right),
 \quad -2\le w\le2,\quad 0\le j<\lfloor N/2\rfloor .
 \quad}                                                          \tag{2}
\]
Every fixed derivative in the ordinary variable \(w\) has the same
rate with polynomial cost. A sufficiently small fixed complex
neighborhood of the real \(w\)-interval costs an arbitrarily small
positive rate allowance. No derivative assertion in the discrete
physical index is made.

For the original coefficients in
[high-Newton contraction, Proposition 4](research_high_newton_radical_contraction.md)
and [terminal insertion, equations (1)--(5)](research_mixed_next_high_coefficients_terminal_insertion.md),
\[
 \ell_b(w)=\sum_{j=0}^{D-b}b_{D-b,j}\mathcal R_N(c_j)^3
                                  \mathcal K_{3,N}(w,c_j),
 \qquad |b_{nj}|\le2,
                                                                  \tag{3}
\]
the same bound holds whenever \(D-b<\lfloor N/2\rfloor\).
In particular it applies to the whole unresolved middle right band.

## 2. A complex Newton envelope with every index retained

Write
\[
 J(y)=\int_0^y\log(2\sin\pi t)\,dt,\qquad
 V_0(y)=J(2y)-4J(y)\quad(0\le y\le1/2),
 \qquad b_2=V_0(1/4).
                                                                  \tag{4}
\]
For \(z=\theta-ih\), \(h\ge0\), define on the full index interval
\[
 V_z(y)=\int_0^y
       \log|2\cos(2\pi t)+2\cos z|\,dt-2J(y),
 \qquad 0\le y\le1 .                                             \tag{5}
\]
The same midpoint proof as
[real-period Newton, Lemma 1](research_three_crossing_real_period_newton_bound.md)
gives the uniform upper bound
\[
 |e_k(-2\cos z)|\le CN^A e^{NV_z(k/N)}
       \quad(|\theta|\le\pi,\ 0\le h\le1/2).
                                                                  \tag{6}
\]
For completeness, factor the numerator into the two shifted cosine
products. Away from their closest mesh cells to a zero, the
logarithmic derivative is bounded by a constant divided by complex
distance to that zero, and its summed midpoint error is
\(O(\log N)\). In the bounded number of closest cells, a height
at least \(N^{-1}\) removes the singularity and gives the same
bound. At a smaller height, rescaling the cell gives a sampled
logarithm at most \(-\log N+C\) and an integral average at least
\(-\log N-C\). Exact numerator zeros only reduce the sampled
product. The original sine-factorial denominator has its uniform
\(O(\log N)\) error. This proves (6), including \(h=0\).

Put \(C_h=\cosh h\), \(c=\cos(2\pi y)\), and
\(s=\sin(2\pi y)\). The following identities or inequalities
will be used only on \(0\le y\le1/2\):
\[
\begin{split}
 V_z(y)&\ge V_\theta(y)\ge0,\\
 V_z(1-y)&=h-V_z(y),\\
 V_{-ih}(y)-V_0(y)&\le
             \frac{\cosh h-1}{2\pi}\tan(\pi y),
                         \qquad 0\le y<1/2 .
\end{split}                                                       \tag{7}
\]
The first inequality follows directly from
\[
 \partial_h|c+\cos(\theta-ih)|^2
                  =2\sinh h\,(c\cos\theta+\cosh h)\ge0.
\]
The remaining nonnegativity is real-period Newton, Lemma 2.
For the reflection in (7), the full-period numerator integral is
\(h\), by factoring it into two circle logarithms of radius
\(e^{-h}\); its integrand is symmetric under \(t\mapsto1-t\).
Use also \(J(1-y)=-J(y)\).
Finally,
\[
 \partial_h V_{-ih}(y)
 =\int_0^y\frac{\sinh h}{\cos(2\pi t)+\cosh h}\,dt
 \le \frac{\sinh h}{2\pi}\tan(\pi y),
\]
which proves the last line of (7).

Define the lower-half combined exponent
\[
 L(y,z)=V_0(y)+V_z(y).
\]
For \(0\le h\le1/2\), it decreases in \(y\) on
\([4/15,1/2]\). Indeed \(\cosh(1/2)<8/7\) and
\(c\le\cos(8\pi/15)<-1/10\), so
\[
 e^{\partial_yL}
 =\frac{(1+c)|c+\cos z|}{(1-c)^2}
 \le\frac{(1+c)(8/7-c)}{(1-c)^2}<1 .                            \tag{8}
\]
The numerator minus denominator in the last comparison is
\[
 \frac17+\frac{15}7c-2c^2\le-\frac{16}{175}<0.
\]
The elementary constants can be checked without evaluating a root:
\[
 \cosh(1/2)
 <1+\frac18+\frac{1/384}{1-1/120}
 =\frac{2147}{1904}<\frac87,
\]
and
\(\sin(\pi/30)>5/48-1/4374>1/10\).

For each real \(w\), real-period Newton gives coefficient exponent
at most \(V_0(y)\) below half and at most zero above half.
At a physical \(c_j\) in (2), the coefficients vanish for \(k>j\),
and every remaining coefficient is between zero and \(e_k(-2)\).
Combining these facts with (6)--(8) gives
\[
 \left|K_N(w,-2\cos z)K_N(c_j,-2\cos z)\right|
 \le CN^A e^{2NM(\theta,h)},
\]
\[
 M(\theta,h)=\max\left\{
 h,\ \max_{0\le y\le4/15}L(y,\theta-ih)\right\}.
                                                                  \tag{9}
\]
The term \(h\) explicitly retains the whole upper Newton half:
its ordinary-color coefficient exponent is nonpositive and, by
(7), its complex Newton exponent is at most \(h\).

## 3. The shifted horizontal

Set \(a=4/3\). The estimates below first use
\(0\le\theta\le a\); evenness of the modulus makes the negative
part cheaper after the chirp is attached.
On \(1/6\le y\le4/15\), direct differentiation of (5) gives
\[
 \partial_\theta V_{\theta-ih}(y)
 =-\frac1{2\pi}\operatorname{artanh}
       \frac{s\sin\theta}{C_h+c\cos\theta}
 \le-\frac6{23\pi}\sin\theta .                                \tag{10}
\]
Here \(s\ge\sqrt3/2>6/7\) and
\(C_h+c\cos\theta\le8/7+1/2=23/14\).
The ratio is in \([0,1)\) at positive height; the real-height
limit is interpreted by continuity through integrable zeros.
Also
\(\tan(4\pi/15)<6/5\): write
\(4\pi/15=\pi/4+\pi/60\), and use
\(\tan(\pi/60)<36/647<1/11\).
Thus
\[
 L(y,\theta-ih)
 \le2b_2+\frac{3(C_h-1)}{5\pi}
                   -\frac6{23\pi}(1-\cos\theta).
                                                                  \tag{11}
\]

On \(0\le y\le1/6\), use
\[
 V_0''(y)=-\frac{4\pi}{\sin(2\pi y)}\le-4\pi,
 \qquad b_2-V_0(y)\ge\frac\pi{72},
 \qquad \tan(\pi y)\le1/\sqrt3<3/5.
\]
The angular derivative is nonpositive throughout the lower half,
so (7) gives
\[
 L(y,\theta-ih)
 \le2b_2-\frac\pi{36}+\frac{3(C_h-1)}{10\pi}.
                                                                  \tag{12}
\]

At \(h=1/2\), the charge-one trace exponential adds
\(-1/2+3\theta/(4\pi)\) to twice (11) or (12).
The expression from (11) increases in \(\theta\), since
\(3/4-12\sin\theta/23>0\).
Using \(\cos(4/3)<1/4\), \(\pi>25/8\), and the proved
\(b_2<729/1250\) from
[real-period Newton, equation (20)](research_three_crossing_real_period_newton_bound.md),
its upper rate is
\[
 E_{\rm large}
 <\frac{1458}{625}-\frac12+\frac{5024}{20125},
 \qquad
 \frac{419}{200}-
 \left(\frac{1458}{625}-\frac12+\frac{5024}{20125}\right)
 =\frac{10111}{805000}>\frac1{80}.
                                                                  \tag{13}
\]
The bound \(\cos(4/3)<1/4\) follows already from the alternating
Taylor upper bound \(59/243<1/4\).
For (12), \(\pi>3\) gives the cheaper rate
\[
 E_{\rm small}<4b_2-\frac{32}{105}
                        <\frac{419}{200}-\frac1{20}.
                                                                  \tag{14}
\]
The upper-Newton alternative \(M=h\) contributes at most
\(1/2+1/\pi<5/6\). Thus every original Newton index is
included in (13)--(14).

## 4. Removed real samples and the complete vertical current

On the real period, the same source estimates give
\[
 |K_N(w,-2\cos\theta)K_N(c_j,-2\cos\theta)|
 \le CN^A e^{N\{2b_2+2m(\theta)\}},
 \qquad
 m(\theta)=\max_yV_\theta(y).
                                                                  \tag{15}
\]
Real-period Newton, equation (16), with
\(\cos(a/2)=\cos(2/3)<4/5\), proves
\[
 2b_2+2m(a)
 <\frac{1458}{625}-\frac{3052}{12375}
 =\frac{129082}{61875},
 \qquad
 \frac{419}{200}-\frac{129082}{61875}
 =\frac{4369}{495000}>\frac1{125}.
                                                                  \tag{16}
\]
One may use
\(\cos(2/3)\le191/243<4/5\) in that calculation.
The polynomial product in (15) is uniformly bounded at this rate
on the ordinary interval \([-2\cos a,2]\).
Markov's inequality there controls its derivative at polynomial
cost. Therefore (16) pays the complete derivative-sampling terms
at every removed real angle \(|\theta|\ge a\), including all
physical normals.

It remains to pay, rather than discard, the vertical side. For
\(0\le y\le4/15\) and \(0\le h\le1/2\),
\[
 \partial_h^2 V_{a-ih}(y)
 =\frac{\sin(2\pi y)}{2\pi}
          \Re\frac1{\cos(2\pi y)+\cos(a-ih)}\ge0 .
                                                                  \tag{17}
\]
The denominator has positive real part. Explicitly,
\[
 \cos a>\frac29,\qquad
 \cos(8\pi/15)>-\frac{11}{105},\qquad
 \frac29-\frac{11}{105}>0.
\]
For the first inequality use the degree-six alternating lower
bound \(7709/32805>2/9\).
Consequently \(M(a,h)\) in (9) is convex in \(h\): it is the
maximum of the linear function \(h\) and convex functions (17).
The vertical trace rate
\[
             2M(a,h)-h\left(1-\frac{3a}{2\pi}\right)
                                                                  \tag{18}
\]
is convex as well. Its maximum on \([0,1/2]\) occurs at an
endpoint. Equations (16) and (13)--(14) pay those two endpoints.
The opposite vertical height has a smaller chirp modulus, so (18)
controls it too.

## 5. Exact finite trace assembly

Choose the original half-grid endpoint
\[
 m_N=\left\lfloor\frac{N(\pi-a)}{2\pi}\right\rfloor,
 \qquad a_N=\pi-\frac{2\pi m_N}{N}\ge a,
 \qquad a_N=a+O(N^{-1}).
                                                                  \tag{19}
\]
For the complete two-kernel input
\(f_N(\theta)=K_N(w,-2\cos\theta)K_N(c_j,-2\cos\theta)\),
put
\[
 g_N(\theta)=\sin\theta\,f_N(\theta)
                     e^{3iN\theta^2/(4\pi)},\qquad
 W_N(\theta)=\frac{e^{-iN\theta}}
                    {(1-\eta e^{-iN\theta})^2}.
\]
The retained part of the original trace is exactly
\[
 -\frac{N^2q^{3D^2/4}}{\pi i}
       \int_{-a_N-i/2}^{a_N-i/2}g_N(\theta)W_N(\theta)\,d\theta
 +\frac{\eta N^2q^{3D^2/4}}\pi
       \int_{-1/2}^{1/2}
        \frac{g_N(a_N+iv)}{4\cosh^2(Nv/2)}\,dv .
                                                                  \tag{20}
\]
This is
[the complete trace, Corollary 3](research_exact_complete_trace_contour.md),
not a principal-charge approximation. Its complementary terms are
the literal original derivative samples outside \((-a_N,a_N)\).

On the horizontal,
\[
 |W_N(\theta)|\le
       \frac{e^{-N/2}}{(1-e^{-N/2})^2}.
\]
This bounds all positive Fourier charges together, with their
original charge multiplicities. Equations (13)--(14) therefore
pay the entire first integral in (20). The reciprocal denominator of
the vertical integral is at most \(e^{-N|v|}\), so (18) pays that
entire integral. All inequalities used at \(a\) have fixed strict
margins and hold at \(a_N\), with an \(O(N^{-1})\) change in
rate. In particular the convexity argument is uniform on a fixed
neighborhood of \(a\). Equation (16) pays every removed sample.
Uniform product errors, integration lengths, scalar factors, and
the number of samples cost only a power of \(N\). This proves (2).

At odd levels the original sample at zero retains its simple-root
value; at even levels the two nearest nonzero samples retain the
double normal. Both are enclosed by (20). No positivity of their
signed sum is assumed. Markov in the complete ordinary variable
\(w\), and polynomial continuation from \([-2,2]\), give the
derivative and small-neighborhood assertions following (2).
Equation (3), its polynomial number of terms, and
\(|\mathcal R_N(c_j)|=1\) prove its stated consequence.

## 6. Remaining original observation

The right observation still attaches to (3) the original factor
\[
                 \frac{(-q)^b}{\kappa^2N}C_{0,N}(r^b,Z)
\]
and sums over its prescribed physical band. The bound (2) does
not bound that last operation at the required action. Taking
absolute values there would still require the outgoing positive
sum, while keeping it coherent requires a further estimate.
No new \(+N\) is added to this normalization.

Thus the exact Fourier contour removes the previously exhibited
\(4b_2\) cost of the inner absolute trace, with a strict bound below
the available action floor for the inner kernel and its actual
high-Newton combination. It does not prove suppression of the
complete middle insertion, nonzero contribution of any trace
critical point, or noncancellation of the full \(343\) transfer.
