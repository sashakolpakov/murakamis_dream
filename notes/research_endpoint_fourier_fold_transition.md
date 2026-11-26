# The Fourier fold after removing an actual top Newton packet

Private written proof, 16 November 2026.

Remove a fixed positive fraction of the highest Newton modes from
the radical of one microscopic endpoint kernel. The remaining upper
Fourier coefficients have positive magnitudes concentrated in a
\(\sqrt N\) window at the frequency fold. We prove a uniform Gaussian
bound, their explicit fold profile, and their total coefficient mass.
The lower coefficients and the full physical normal are then restored
by exact reflection identities. The resulting complex angular bound
still permits exponential growth; no scalar or filled-source gap is
asserted.

## 1. The literal packet and its coefficients

Use
\[
 \theta=\pi/N,\quad D=N-1,\quad \eta=(-1)^D,\quad
 s_j=2\sin(j\theta),\quad S_j=\prod_{r=1}^j s_r,\quad S_0=1,
\]
\[
 c_j=2\cos((2j+1)\theta),\quad
 e_j(Z)=S_j^{-2}\prod_{h<j}(c_h-Z),\quad
 P_N(Z)=2T_N(Z/2)+2 .
 \tag{1}
\]
Fix \(0<\varepsilon<1/2\), a finite \(A\), and real
\(|\alpha|\le A\). Put
\[
 w=2\cosh(\alpha/N),\qquad p_N=\lfloor N/2\rfloor,\qquad
 M_N=\lfloor\varepsilon N\rfloor .
 \tag{2}
\]
The exact removed and remaining radical packets are
\[
 \mathcal T_N(Z)=\sum_{m=1}^{M_N}e_{N-m}(w)e_{N-m}(Z),\qquad
 \mathcal H_N(Z)=\sum_{m=M_N+1}^{p_N}
                         e_{N-m}(w)e_{N-m}(Z).
 \tag{3}
\]
An empty sum is zero. Thus the full original kernel after this
removal is \(K_N^{\rm low}(w,Z)+\mathcal H_N(Z)\), not
\(\mathcal H_N\) alone. The cutoff is an actual Newton cutoff.

Write
\[
 \mathcal H_N(-2\cos t)
       =h_{0,N}+2\sum_{k=1}^{D}h_{k,N}\cos(kt).
\]
For \(M_N<s\le p_N\), the exact positive coefficient formula of
the bulk Fourier source gives
\[
 h_{N-s,N}=\eta(-1)^{s-1}B_{s,N},\qquad
 B_{s,N}=\sum_{m=M_N+1}^{s}T_{m,s,N}>0,
 \tag{4}
\]
\[
 T_{m,s,N}=
 \frac{P_N(w)S_{m-1}^4}{N^4}
 \frac{S_{s+m-1}}
 {S_{s-m}S_{2m-1}\prod_{h<m}(w-c_h)}.
 \tag{5}
\]
For \(s\le M_N\), set \(B_{s,N}=0\). All estimates below are
uniform in real \(\alpha\) in (2), for sufficiently large \(N\).
Their level threshold may depend on \(\varepsilon,A\).

For every physical double node \(c_a\), the original radical
normal of \(e_{N-m}\) has support \(a\le m-1\).
Consequently the removed packet \(\mathcal T_N\) has zero
value at every physical node and zero normal at every \(a\ge M_N\).
In particular \(K_N-\mathcal T_N\) retains the full original
physical value and first normal at those latter nodes. The
odd simple-node value is retained everywhere. These are exact
source statements, not estimates.

## 2. Exact ratio factorization and a global Gaussian bound

Let
\[
 d=N/2-s\ge0,\qquad a_N=\sinh^2(\alpha/(2N)),\qquad
 \zeta_{d,N}=\sin^2(\pi d/N).
\]
The positive summands have the exact factorization
\[
 T_{m,s,N}=T_{1,s,N}\,
       A_{m,N}^{\,3} C_{m,N}D_{m,d,N}E_{m,\alpha,N},
 \tag{6}
\]
where all products below run from \(j=1\) to \(m-1\):
\[
 A_{m,N}=\prod_j
           \frac{\sin(j\theta)}{\sin((j+\tfrac12)\theta)},
 \qquad
 C_{m,N}=\prod_j
           \frac{\cos(j\theta)}{\cos((j+\tfrac12)\theta)},
\]
\[
 D_{m,d,N}=\prod_j
       \left(1-\frac{\zeta_{d,N}}{\cos^2(j\theta)}\right),
 \qquad
 E_{m,\alpha,N}=\prod_j
       \left(1+\frac{a_N}{\sin^2((j+\tfrac12)\theta)}\right)^{-1}.
 \tag{7}
\]
Every factor is positive in the physical range \(m\le s\).
Indeed the ratio of successive summands is
\[
 \frac{T_{j+1,s,N}}{T_{j,s,N}}
 =\left(\frac{\sin(j\theta)}
               {\sin((j+\tfrac12)\theta)}\right)^3
   \frac{\cos(j\theta)}{\cos((j+\tfrac12)\theta)}
   \left(1-\frac{\zeta_{d,N}}{\cos^2(j\theta)}\right)
   \left(1+\frac{a_N}{\sin^2((j+\tfrac12)\theta)}\right)^{-1}.
 \tag{8}
\]
This follows from (5), \(w-c_j=4\{\sin^2((j+1/2)\theta)+a_N\}\),
and
\(\sin((s+j)\theta)\sin((s-j)\theta)
 =\cos^2(j\theta)-\zeta_{d,N}\).

There are absolute constants in
\[
 A_{m,N}\le C m^{-1/2},\qquad
 C_{m,N}\le C\left(\frac{N}{N/2-m+1}\right)^{1/2}.
 \tag{9}
\]
Here is an elementary product justification, including the last
physical value of \(m\). The function \(f(v)=\sin v/v\) decreases
and stays positive on \([0,\pi/2]\). Splitting \(A_{m,N}\) into
\(\prod j/(j+1/2)\) and its \(f\)-ratios, the latter product is
at most \(\pi/2\): its logarithm is the integral of
\(-(\log f)'\) on disjoint half-step intervals. Also
\[
 \prod_{j=1}^{m-1}\frac{j}{j+1/2}
       =\frac{2^{2m-1}}{m\binom{2m}{m}}\le C m^{-1/2}.
 \tag{10}
\]
For \(C_{m,N}\), put \(v=N/2-m\). Reflecting each cosine to a sine
and using the same decreasing \(f\) bounds it by
\[
 \prod_{j=1}^{m-1}\frac{N/2-j}{N/2-j-1/2}
 =\frac{\Gamma(N/2)}{\Gamma(N/2-1/2)}
       \frac{\Gamma(v+1/2)}{\Gamma(v+1)}.
 \tag{11}
\]
For integer and half-integer \(v\ge0\), the elementary factorial
or Wallis product bounds make (11) at most
\(C\sqrt{N/(v+1)}\). Equivalently, taking logarithms of its
factors and comparing their harmonic sums gives
\(\tfrac12\log\{N/(v+1)\}+O(1)\). Thus no positive distance
from the fold is needed in (9).

The first summand is uniformly at most \(C_A/N\), by its exact
formula
\[
 T_{1,s,N}=
 \frac{4\cosh^2(\alpha/2)\,2\sin(s\theta)}
 {N^4(2\sin\theta)\{2\cosh(\alpha/N)-2\cos\theta\}}.
 \tag{12}
\]
Further,
\[
 E_{m,\alpha,N}\le1,\qquad
 D_{m,d,N}\le
             \exp\{-(m-1)\zeta_{d,N}\}.
 \tag{13}
\]
For \(m>M_N\), eventually \(m-1\ge\varepsilon N/2\), and
\(\sin(\pi d/N)\ge2d/N\). Combining (6)--(13) gives
\[
 T_{m,s,N}\le
 \frac{C_{\varepsilon,A}N^{-2}}
                {\sqrt{N/2-m+1}}\,
                     e^{-2\varepsilon d^2/N}.
 \tag{14}
\]
Since the sum of \((N/2-m+1)^{-1/2}\) is \(O(\sqrt N)\),
we have proved the following uniform statement.

**Theorem 1.** At both parities and every physical \(s\),
\[
 0\le B_{s,N}\le
 C_{\varepsilon,A}N^{-3/2}
             \exp\{-2\varepsilon(N/2-s)^2/N\}.
 \tag{15}
\]
In particular a fixed distance \(\delta N\) below the fold gives
the upper bound
\(C_{\varepsilon,A}N^{-3/2}e^{-2\varepsilon\delta^2N}\).
The assertion concerns the actual complementary coefficients in
(4), with the top packet in (3) removed.

## 3. The fold profile with its calibrated amplitude

Put \(u_{s,N}=(N/2-s)/\sqrt N\). Define
\[
 \mathcal F_{\varepsilon,\alpha}(u)
   =\frac{\cosh(\alpha/2)}{2\pi}
        \int_{\tan(\pi\varepsilon)}^\infty
                   v^{-3/2}e^{-\pi u^2v}\,dv,\qquad u\ge0 .
 \tag{16}
\]
This is positive, continuous at zero, and
\[
 \mathcal F_{\varepsilon,\alpha}(0)
           =\frac{\cosh(\alpha/2)}
                   {\pi\sqrt{\tan(\pi\varepsilon)}}.
 \tag{17}
\]

**Theorem 2.** For each fixed \(U<\infty\),
\[
 \sup_{\substack{M_N<s\le p_N,\ u_{s,N}\le U\\|\alpha|\le A}}
 \left|N^{3/2}B_{s,N}
              -\mathcal F_{\varepsilon,\alpha}(u_{s,N})\right|
                              \longrightarrow0.
 \tag{18}
\]
The fold lattice for \(d=N/2-s\) is the nonnegative integers
when \(N\) is even and the positive half-integers when \(N\)
is odd. Both are included in the same uniform limit.

**Proof.** First take \(m/N=y\) in a fixed compact subinterval
of \((0,1/2)\), and \(u_{s,N}\le U\).
We prove
\[
 T_{m,s,N}
 =\frac{\cosh(\alpha/2)}{2N^{5/2}}\,
   \frac{\exp\{-\pi u_{s,N}^2\tan(\pi y)\}}
        {(\sin\pi y)^{3/2}(\cos\pi y)^{1/2}}
                       \{1+O(N^{-1})\},
 \tag{19}
\]
uniformly on that compact set.

The constant in (19) is fixed by finite original products. Define
\[
 Q_{m,N}(\alpha)=
    \prod_{j=0}^{m-1}
       \left(1+\frac{a_N}{\sin^2((j+1/2)\theta)}\right).
\]
The exact physical polynomial identity
\(P_N(w)/P_N(2)=\cosh^2(\alpha/2)\), with its double roots
and its odd simple root retained, gives
\[
 Q_{p_N,N}(\alpha)=
 \begin{cases}
 \cosh(\alpha/2),&N\text{ even},\\
 \cosh(\alpha/2)/\cosh(\alpha/(2N)),&N\text{ odd}.
 \end{cases}
 \tag{20}
\]
All factors are positive for real \(\alpha\), which fixes the
square root in this equality. For \(m/N\) in the present compact
set, the omitted factors with \(j\ge m\) have total logarithm
\(O(N^{-1})\): each is \(1+O_A(N^{-2})\). Hence
\[
 Q_{m,N}(\alpha)=\cosh(\alpha/2)\{1+O(N^{-1})\}.
 \tag{21}
\]
Combining the \(j=0\) factor with (12) yields exactly
\[
 T_{1,s,N}E_{m,\alpha,N}
 =\frac{P_N(w)\cos(d\theta)}
        {4N^4\sin\theta\,\sin^2(\theta/2)}
                         Q_{m,N}(\alpha)^{-1}
 =\frac{4\cosh(\alpha/2)}{\pi^3N}
                              \{1+O(N^{-1})\}.
 \tag{22}
\]
Here \(d=u_{s,N}\sqrt N\), so \(\cos(d\theta)=1+O(N^{-1})\).

For the sine product, use the exact rational factor in (10).
Its factorial asymptotic is
\(\sqrt\pi/(2\sqrt m)\{1+O(m^{-1})\}\).
If \(f_1(x)=\sin(\pi x)/(\pi x)\), the logarithm of its
remaining smooth product is
\[
 \sum_{j=1}^{m-1}
  [\log f_1(j/N)-\log f_1((j+1/2)/N)]
       =-\tfrac12\log f_1(y)+O(N^{-1}).
 \tag{23}
\]
This follows by Taylor's formula followed by a Riemann sum;
\(f_1(0)=1\), and its logarithm is smooth on the relevant compact
interval. Thus
\[
 A_{m,N}=
        \frac{\pi}{2\sqrt{N\sin(\pi y)}}\{1+O(N^{-1})\}.
 \tag{24}
\]
The analogous smooth calculation for \(\log\cos(\pi x)\) gives
\[
 C_{m,N}=(\cos\pi y)^{-1/2}\{1+O(N^{-1})\}.
 \tag{25}
\]
Finally
\[
 \zeta_{d,N}=\pi^2u_{s,N}^2/N+O_U(N^{-2}),\qquad
 \sum_{j=1}^{m-1}\sec^2(j\theta)
                       =\frac N\pi\tan(\pi y)+O(1).
 \tag{26}
\]
The quadratic error in expanding the logarithm of \(D\) is
\(O(N^{-1})\) on the fixed compact set. Therefore
\[
 D_{m,d,N}
       =e^{-\pi u_{s,N}^2\tan(\pi y)}\{1+O(N^{-1})\}.
 \tag{27}
\]
Equations (22), (24), (25), and (27) prove (19), including
its constant and both parity normalizations.

It remains to sum through the actual last term \(m=s\).
For any small fixed \(\delta>0\), (14) gives
\[
 N^{3/2}
   \sum_{\substack{m\le s\\m/N>1/2-\delta}}T_{m,s,N}
             \le C_{\varepsilon,A}(\sqrt\delta+N^{-1/2}),
 \tag{28}
\]
uniformly in the stated \(u\)-window. The proposed integral in
\(y\) has the same uniformly integrable upper endpoint, because
its exponential is at most one and its singularity is
\((1/2-y)^{-1/2}\). On
\([\varepsilon,1/2-\delta]\), (19) and ordinary uniform Riemann
sums apply; the lower grid displacement \(M_N/N-\varepsilon\)
is \(O(N^{-1})\). Sending \(N\) to infinity and then \(\delta\)
to zero proves uniform convergence to
\[
 \frac{\cosh(\alpha/2)}2
 \int_\varepsilon^{1/2}
  \frac{e^{-\pi u^2\tan(\pi y)}}
       {(\sin\pi y)^{3/2}(\cos\pi y)^{1/2}}\,dy.
 \tag{29}
\]
The substitution \(v=\tan(\pi y)\) turns (29) into (16).
This proves (18). \(\square\)

## 4. Coefficient mass and the exact reflected normal channel

The Gaussian bound (15) also controls arbitrarily large \(u\).
Consequently (18), applied on fixed \(u\)-windows and then
combined with Gaussian tail domination, gives
\[
 N\sum_{s=M_N+1}^{p_N}B_{s,N}
       \longrightarrow
       \int_0^\infty\mathcal F_{\varepsilon,\alpha}(u)\,du
       =\frac{\cosh(\alpha/2)}{4\pi\tan(\pi\varepsilon)}.
 \tag{30}
\]
The convergence is uniform for real \(|\alpha|\le A\).
Indeed the \(u\)-mesh is \(N^{-1/2}\) at both parities, and
\(\int_0^\infty e^{-\pi vu^2}du=1/(2\sqrt v)\) evaluates
the final integral.

Because \(\mathcal H_N\) vanishes at every physical value,
its lower Fourier coefficients are not independent:
\[
 h_{0,N}=0,\qquad
              h_{s,N}=-\eta h_{N-s,N}\quad(1\le s<N/2).
 \tag{31}
\]
One proof substitutes all \(N\) distinct angular grid points
\(z^N=\eta\) in its Laurent polynomial and uses their finite
Fourier independence. For \(1\le s<N/2\), the two frequencies
fold to \(h_s+\eta h_{N-s}\); the constant coefficient has
no other alias because the Laurent degree is below \(N\).
At even \(N\), the middle cosine vanishes at every grid point
and its coefficient is supplied by (4).

Set
\[
 \omega_{s,N}=
 \begin{cases}
 1/2,&N\text{ even and }s=N/2,\\
 1,&\text{otherwise}.
 \end{cases}
\]
The complete exact ordinary identity is therefore
\[
 \mathcal H_N(-2\cos t)
 =2\sum_{s=M_N+1}^{p_N}
     \omega_{s,N}(-1)^s B_{s,N}
                [\cos(st)-\eta\cos((N-s)t)].
 \tag{32}
\]
The half weight prevents double counting the even middle frequency.
Every nonzero Laurent coefficient has sign \((-1)^k\) at
frequency \(k\). Hence its full Laurent coefficient norm satisfies
\[
 \|\widehat{\mathcal H}_N\|_1
     =4\sum_s\omega_{s,N}B_{s,N}
     =\mathcal H_N(2)
     =\sup_{t\in\mathbb R}|\mathcal H_N(-2\cos t)|,
\]
\[
 N\|\widehat{\mathcal H}_N\|_1
       \longrightarrow\frac{\cosh(\alpha/2)}
                              {\pi\tan(\pi\varepsilon)}.
 \tag{33}
\]
The even half weight changes (30) only by \(O(N^{-1/2})\)
after multiplication by \(N\).

At a physical double node put
\[
 \tau_a=\pi-(2a+1)\pi/N,\quad c_a=-2\cos\tau_a,\qquad
 q_a=(2a+1)\pi/N .
\]
Differentiate (32) before specialization. Since
\(\cos(N\tau_a)=\eta\), \(\sin(N\tau_a)=0\), its paired derivative
is \(-N\sin(s\tau_a)\). Also
\((-1)^s\sin(s\tau_a)=-(-1)^a\cos((N/2-s)q_a)\).
The original normal weight is thus exactly
\[
 \boxed{\quad
 \eta(4-c_a^2)\mathcal H_N'(c_a)
   =4\eta N(-1)^a\sin\tau_a
        \sum_{s=M_N+1}^{p_N}\omega_{s,N}B_{s,N}
                         \cos((N/2-s)q_a).
 \quad}
 \tag{34}
\]
The prime on \(\mathcal H_N\) is the ordinary spectral derivative.
In particular, for any actual spectator \(f\),
\[
 \phi_N(\mathcal H_N f)
   =\sum_{a=0}^{p_N-1}
           \eta(4-c_a^2)\mathcal H_N'(c_a)f(c_a).
 \tag{35}
\]
All other traces and ordinary boundary variables may remain in
\(f\), as may every original crossing factor. The odd simple
node contributes zero. The source identities also hold at \(N=2\),
where \(e_1(Z)=-Z/4\); the asymptotic statements concern large
levels.

Equations (32)--(35) retain the actual normal-defect channel.
The uniform error \(o(1)\) in (18) alone is not an asymptotic
for the highly oscillatory cosine sum in (34). No such conclusion
is taken before that coherent sum, its spectators, and its
original closing have been controlled.

## 5. A complex angular envelope and its limit

Let \(H=|\Im t|\). The exact frequencies in (32) are at most
\(N/2+d\), where \(d=N/2-s\). By (15), completing the square gives
\[
 \begin{split}
 |\mathcal H_N(-2\cos t)|
 &\le C_{\varepsilon,A}N^{-3/2}e^{NH/2}
                  \sum_d e^{-2\varepsilon d^2/N+Hd}\\
 &\le C_{\varepsilon,A}N^{-1}
          \exp\left\{N\left(\frac H2+\frac{H^2}{8\varepsilon}\right)\right\}.
 \end{split}
 \tag{36}
\]
The Gaussian sum centered at \(NH/(4\varepsilon)\) is
\(O_\varepsilon(\sqrt N)\), uniformly in its center and on
either the integer or half-integer lattice. Thus (36) holds
for every complex \(t\). Each fixed angular derivative adds
at most the corresponding power of \(N\).
One may also keep the actual range \(0\le d\le N/2-M_N-1\)
when maximizing the exponent. The separate trivial frequency
bound from (33) is
\[
 |\mathcal H_N(-2\cos t)|
       \le C_{\varepsilon,A}N^{-1}e^{N(1-\varepsilon)H}.
 \tag{37}
\]
These are bounds for the remaining ordinary radical packet.
They do not supply a source gap: a fixed nonzero height still
has an extensive upper exponent. In an original graph the low
kernel, all other factors, and the exact traced normal expression
(35) remain. Shared endpoint products are not replaced by the
single-kernel positive coefficient law.

## 6. Direct sources and proof scope

The following complete direct texts were read at these matching
versions and every used implication was checked:

* [Exact bulk endpoint Fourier coefficients](research_endpoint_bulk_fourier_interpolation.md),
  SHA256 4f92c6081bf67646a14181bb753a903cf615d16adcd8d56d1534842303adb7eb:
  the exact positive coefficient sum, its checkerboard sign,
  and the literal consecutive-term ratio.
* [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  the actual radical range, its physical value and normal support,
  and the original full-normal closing functional.

The new statements are the uniform complementary fold profile,
its finite-product normalization, coefficient concentration and
mass, and their exact placement in the reflected normal channel.
Only written mathematics, source reads, and hashes were used.
No mathematical program, numerical experiment, test, or build was
run. Previously adopted notes and public manuscripts are unchanged.
