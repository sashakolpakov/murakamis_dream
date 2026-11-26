# Fractional boundary data for the original four-input scalar

22 November 2026. Written research proof. Earlier author-final notes and
public manuscripts remain unchanged.

We retain the full finite pole packet that replaces the three-input
Cauchy pole when one boundary angle is of order \(N^{-1}\).
A second finite rectangle evaluates this packet. Its right connector
has a smaller exponential rate; it is not discarded as a polynomial
error. The resulting estimate concerns the original scalar.

## 1. Source and statement

Use the original source and conventions of [B]:
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad\kappa=e^{\pi i d^2/(2N)},\qquad
 U_x=\sum_{j=0}^d x^jf_j .
 \tag{1}
\]
The full repeated-root algebra and its original Frobenius functional
\(\phi\) are retained. Fix a compact set of triples satisfying
\[
 b,c>0,\quad S=b+c<1,\qquad
                 1-S<R<1-\max(b,c).
 \tag{2}
\]
Put
\[
 \begin{gathered}
 y=-e^{-2\pi ib},\quad z=-e^{-2\pi ic},\quad
 r=e^{-2\pi iR},\quad p=NR,\quad L=N-p,\quad u=1-R,\\
 a\in\mathcal A=[a_-,a_+]\Subset(0,\infty),\qquad
 s_a=-e^{-2\pi i(a-1/2)/N},\quad t_a=r/s_a,\\
                    \Phi_a=\phi(U_yU_zU_{s_a}U_{t_a}).
 \end{gathered}
 \tag{3}
\]
Thus \(a=1\) is the exact unit readout of [B]. Define
\[
 \mathfrak g(b,c,u)=
 \frac{\sin^2(\pi u)\sin(\pi b)\sin(\pi c)}
      {\pi^2\sin(\pi(u-b))\sin(\pi(u-c))}>0 .
 \tag{4}
\]
All constants below are uniform on the fixed compact set and on
\(\mathcal A\). Enlarge this interval to include \(1\), if necessary.

**Theorem.** For all sufficiently large \(N\), the original source
\(\Phi_1\) is nonzero, and
\[
 \boxed{\qquad
 \frac{\Phi_a}{\Phi_1}
  =\frac{N^{2a-2}}{\Gamma(a)^2}\,
                  \mathfrak g(b,c,u)^{a-1}
                         (1+O(N^{-1})).
 \qquad}
 \tag{5}
\]
In particular the entire displayed boundary layer is nonzero.
The powers of the positive number in (4) use its real logarithm.
The baseline in (5) is the actual three-input source,
\[
             \Phi_1=\kappa\sqrt N\,\mathcal C_N(y,z,-qr).
 \tag{6}
\]
The four unit-circle inputs have norm \(\sqrt N\); dividing each
scalar in (5) by \(N^2\) leaves the same ratio. All phases and
internal Hermite normals belong to the original scalar. No transport
through a boundary fold or arbitrary further attachment is claimed.

## 2. Canonical factorial estimates used below

Write \(\mathscr F_N\) for the canonical factorial of [P, equations
(9)--(11)], to distinguish it from the polynomial \(F_N\) in [B].
Its exact identities are
\[
 \begin{gathered}
 \mathscr F_N(0)=1,\quad \mathscr F_N(j)=(Q;Q)_j,\\
 \mathscr F_N(w+1)=(1-Q^{w+1})\mathscr F_N(w),\\
 \mathscr F_N(w+N)=(1-e^{2\pi iw})\mathscr F_N(w),\\
 \mathscr F_N(w)\mathscr F_N(d-w)=Nq^{w(w-d)} .
 \end{gathered}
 \tag{7}
\]
The negative poles start at \(-1\); the first positive zeros are
the simple zeros \(N,\ldots,2N-1\). In particular
\[
               \mathscr F_N'(N+k)=-2\pi i\,\mathscr F_N(k)
                                  \quad(0\le k<N).
 \tag{8}
\]
Let \(f,h\) have their canonical branches from [P]:
\[
 f'(w)=\operatorname{Log}(1-e^{2\pi iw}),\quad
 \Re f(x)=\mathcal L(x),\quad
 h(w)^2=i(1-e^{2\pi iw}),\quad
 \mathcal L(x)=\int_0^x\log|2\sin\pi v|\,dv .
 \tag{9}
\]
The primitive \(\mathcal L\) is extended oddly and periodically.
On fixed strict vertical substrips, for every bounded real shift
\(\tau\),
\[
 \mathscr F_N(Nw+\tau)
 =\sqrt N\,h(w)(1-e^{2\pi iw})^\tau
                         e^{Nf(w)}(1+O(N^{-1})).
 \tag{10}
\]
This is uniform at arbitrary imaginary height. It follows from
[P, equations (32)--(34)] by Taylor expansion; the needed logarithmic
derivatives are bounded there.

We also use (10) when \(\Re w=0,\ |\Im w|\ge\epsilon\).
Here is the extra justification. In the Gamma product defining
\(\mathscr F_N\), the arguments \(Nw,N(m+w),N(m-w)\) remain
in closed sectors excluding the negative real axis and away from
zero. The summed Stirling remainder is bounded by
\[
 CN^{-3}\left(|w|^{-3}
       +\sum_{m\ge1}(|m+w|^{-3}+|m-w|^{-3})\right)
                                      \le C_\epsilon N^{-3}.
 \tag{11}
\]
The identities for the main terms continue from \(\Re w>0\).
This proves (10) on these two additional half-lines with the
continued canonical branches.

At bounded arguments the same Gamma product gives
\[
 \mathscr F_N(v)=(-2\pi i/N)^v\Gamma(v+1)
                  \exp E_N(v),\qquad
 |E_N(v)|\le C(1+|v|)^2/N
 \tag{12}
\]
when \(\Re v\) ranges in a fixed compact subset of \((-1,\infty)\)
and \(|\Im v|\le\epsilon N\), for sufficiently small fixed
\(\epsilon\). For completeness, after the leading Gamma factor is
removed, each paired term is
\[
 \log\frac{\Gamma(Nm+v+1)}
               {\Gamma(Nm-v)(Nm)^{2v+1}}
                         =O((1+|v|)^3/(Nm)^2).
 \tag{13}
\]
The coefficient of \((Nm)^{-1}\) vanishes because the two Gamma
shifts sum to one. Summation and the exact quadratic phase in
\(\mathscr F_N\) prove (12). The logarithm in (12) is continued
from \(v=0\); no Gamma pole meets the uses below.

We also need a fixed-shift comparison at the current endpoint.
For real \(c,c'\) in fixed compact subsets of \((-1,\infty)\),
uniformly for \(|T|\le\epsilon N\),
\[
 \left|\frac{\mathscr F_N(c+iT)}
                  {\mathscr F_N(c'+iT)}\right|
 \le C N^C(1+|T|)^C e^{C|T|/N}.
\]
The ordinary Gamma ratio has only the indicated polynomial cost.
In the paired product (13), taking a fixed difference in the real
shift bounds its logarithm by \(C(1+|T|)^2/N^2\), rather than
the cubic bound for an individual term. Its quadratic phase costs
\(e^{C|T|/N}\). This proves the comparison and justifies using
the exact half-step modulus [P, equation (35)] at other bounded
real endpoint shifts.

These estimates have a useful quantitative consequence. In any
factorial quotient below, all macroscopic real arguments stay in
strict substrips, except specified endpoint factors. For
\(|Y|\ge\epsilon\), apply (10)--(11) to those endpoint factors
as well. The powers of \(1-e^{2\pi iw}\) then determine the
entire remaining height dependence. We will record the resulting
integrable majorants explicitly, rather than use a fixed-\(N\)
asymptotic as an integral bound.

## 3. The exact rectangle retains the third pole family

Set
\[
 \begin{gathered}
 A=N(1-b)-\tfrac12,\quad B_0=N(1-c)-\tfrac12,\quad
 C=N(1-S),\quad A+B_0-C=d,\\
 W(w)=\frac{\mathscr F_N(w)\mathscr F_N(w+C)
                       \mathscr F_N(A)\mathscr F_N(B_0)}
 {\mathscr F_N(C)\mathscr F_N(w+1+A)\mathscr F_N(w+1+B_0)},\\
 K_a(w)=
 \frac{\mathscr F_N(w+a-1)}
      {\mathscr F_N(a-1)\mathscr F_N(w)}
 \frac{\mathscr F_N(w+p-a)\mathscr F_N(p)}
      {\mathscr F_N(p-a)\mathscr F_N(w+p)},\qquad
 T_a(w)=Q^wW(w)K_a(w).
 \end{gathered}
 \tag{14}
\]
The finite source formula [B, equations (9)--(10)] gives exactly
\[
 \Phi_a=\frac{\kappa^2D_N(y)D_N(z)G_N(r)}{N}
                   \sum_{j=0}^dT_a(j),\quad
 D_N(x)=1-\eta x^N,\quad G_N(r)=\sum_{j=0}^d r^j .
 \tag{15}
\]
At \(a=1\),
\[
 Q^wK_1(w)=
       \frac{1-r}{1-rQ^{-w}},
 \tag{16}
\]
which is precisely the three-input Cauchy kernel.

Put \(\delta_*=\min(1/8,a_-/8)\). Choose \(\zeta\) from
\(-\delta_*,-3\delta_*\), so that
\(\operatorname{dist}(p+\zeta,\mathbb Z)\ge\delta_*/2\).
One of these choices always works. Both are greater than \(-a_-\)
and \(-1\). The choice also makes
\(1-r^{-N}e^{2\pi i\zeta}\) uniformly separated from zero.
Put \(K=\lfloor p+\zeta\rfloor\). The sample-preserving differential is
\[
 \Omega_a(w)=\frac{\kappa^2G_N(r)}{N}\,2\pi i\,
 \frac{(1-\eta y^N\tau)(1-\eta z^N\tau)}{\tau-1}
                        T_a(w)\,dw,\qquad \tau=e^{2\pi iw}.
 \tag{17}
\]
Its residue at the integer \(j\) is the \(j\)-th term of
(15). Work first off collisions of integer and moving poles.
The final canceled formulas will remove this restriction.

Use the rectangle \(\zeta<\Re w<N+\zeta\), with horizontal
heights tending to infinity. The two periodic numerator factors
in (17) cancel exactly the two old outer denominator families
from \(\mathscr F_N(w+1+A)\) and
\(\mathscr F_N(w+1+B_0)\), as in [P]. The third family is not
canceled: its poles are
\[
                         w=L+k,\qquad 0\le k\le K.
 \tag{18}
\]
They come from the first zero block of \(\mathscr F_N(w+p)\).
There is no further zero block in the rectangle. The numerator
\(\mathscr F_N(w+a-1)\) has its first negative pole at \(-a\),
strictly to the left of both possible left sides. The other
numerator poles are farther left. This lists every pole.

The horizontal sides do vanish at fixed \(N\). After the common
factor \(\mathscr F_N(w)\) is canceled, \(T_a\) has three
numerator and three denominator factorials. The difference of
their total shifts is \(-N-2\). Including \(Q^w\), its lower
end decays as \(e^{-2\pi(1+1/N)|\Im w|}\).
The degree-two periodic numerator divided by \(\tau-1\) costs
\(e^{2\pi|\Im w|}\) below. Thus both ends retain decay
\(e^{-2\pi|\Im w|/N}\). No degree-three cancellation or
additional periodic denominator has been introduced.

For the paired vertical current, write
\[
 Y_0=y^N,\quad Z_0=z^N,\quad \rho=r^{-N},\quad a_0=e^{2\pi ia},
\]
\[
 \begin{split}
 A_a&=\eta(Y_0+Z_0)+\rho-Y_0Z_0-a_0-\rho/a_0,\\
 B_a&=Y_0Z_0(a_0+\rho/a_0-1)+\rho[1-\eta(Y_0+Z_0)] .
 \end{split}
 \tag{19}
\]
The exact factorial monodromy gives
\[
 \frac{T_a(w+N)}{T_a(w)}
 =\frac{(1-Y_0Z_0\tau)(1-a_0\tau)(1-\rho\tau/a_0)}
 {(1-\eta Y_0\tau)(1-\eta Z_0\tau)(1-\rho\tau)}.
 \tag{20}
\]
Subtracting one cancels both the constant and cubic terms.
Consequently the whole paired current is
\[
 I_a=\frac{\kappa^2G_N(r)}{N}
 \int_{\zeta-i\infty}^{\zeta+i\infty}
 \frac{\tau(A_a+B_a\tau)}{(\tau-1)(1-\rho\tau)}
                                  T_a(w)\,dw .
 \tag{21}
\]
The factor \(A_a+B_a\tau\) remains a numerator. In particular
its zeros have not produced an unrecorded orbit of poles.

Uniformly in the parameters,
\[
                              |I_a|\le C N^C .
 \tag{22}
\]
Here are bounds for this assertion. The rational kernel in (21)
is at most \(C e^{-2\pi N Y}\) for \(Y\ge0\), and at most
\(C\) for \(Y\le0\), on \(w=\zeta+iNY\).
The choice of \(\zeta\) bounds both denominators below by a positive
constant times \(1+|\tau|\). The bounded shifts in \(K_a\), using
(10)--(13), cost at most \(N^C(1+|Y|)^C e^{C|Y|}\) relative
to the old left weight and its Cauchy factor.

For unit \(y,z\), the rate \(R_0\) of [P, equations (37)--(41)]
satisfies \(R_0(Y)\le\pi Y\) on both half-lines. Indeed its
three radii there are equal. For every \(k>0\), the ratio
\[
 Z_k=\frac{(1-ke^{-2\pi ib})(1-ke^{-2\pi ic})}
                    {1-ke^{-2\pi iS}}
 \tag{23}
\]
has positive imaginary part: after clearing its denominator,
the imaginary numerator is
\[
 2k(1+k)\sin(\pi S)
                 [\cos\pi(b-c)-\cos\pi S]>0.
\]
Thus its continuous argument lies in \((0,\pi)\), requiring only
\(b,c>0,S<1\). The proof does not require \(b,c<1/2\).
The current is bounded by
\[
 C N^C\int_{\mathbb R}(1+|Y|)^C
                    e^{-\pi N|Y|+C|Y|}\,dY ,
 \tag{24}
\]
after absorbing the factor \(dw=iN\,dY\) into \(N^C\).
This is a quantitative integrable majorant for (22).

## 4. The exact retained packet and its pole-free amplitude

Define
\[
 D_y=L-Nb+\tfrac12,\qquad D_z=L-Nc+\tfrac12.
 \tag{25}
\]
All of \(A,B_0,C,L,L+C,D_y,D_z,p\), with bounded shifts as
used below, stay in fixed strict factorial strips. The same
quasiperiod identity that canceled the two outer families gives
\[
 (1-\eta y^N\tau)(1-\eta z^N\tau)W(w)
 =\frac{\mathscr F_N(w)\mathscr F_N(w+C)
                         \mathscr F_N(A)\mathscr F_N(B_0)}
        {\mathscr F_N(C)\mathscr F_N(w-Nb+1/2)
                              \mathscr F_N(w-Nc+1/2)}.
 \tag{26}
\]
Using (8) at every pole in (18), with the orientation of the
rectangle, proves the exact decomposition
\[
                         \Phi_a=\mathcal G_a S_{N,a}+I_a,
 \tag{27}
\]
where
\[
 \begin{split}
 S_{N,a}&=\sum_{k=0}^{K}R_k,\qquad
 R_k=\frac{Q^k(Q^{1-a},\,rQ^a,\,Qr yz;Q)_k}
                  {(Q,\,-q^3ry,\,-q^3rz;Q)_k},\\
 \mathcal G_1&=
 \frac{\kappa^2\mathscr F_N(A)\mathscr F_N(B_0)
                         \mathscr F_N(L)\mathscr F_N(L+C)}
      {\mathscr F_N(C)\mathscr F_N(D_y)\mathscr F_N(D_z)},\\
 \frac{\mathcal G_a}{\mathcal G_1}
 &=-\frac r{1-r}\frac{\mathscr F_N(p)}{\mathscr F_N(p-a)}
       \frac{\mathscr F_N(L+a-1)}{\mathscr F_N(L)}
       \frac{q^{(N-a)(1-a)}}{\mathscr F_N(a-1)^2}.
 \end{split}
 \tag{28}
\]
Every denominator in (28) is nonzero in our domain for large \(N\).
The two macroscopic packet denominator families stay uniformly away
from zero, since their factorial intervals lie strictly between
\(0\) and \(N\). The light factor \((Q;Q)_k\) is only asserted
nonzero for \(k<N\); its small factors are retained exactly in the
endpoint Gamma estimates.

To check the source sign and normalization, before cancellation the
residue at \(L+k\) contains
\((1-e^{-2\pi ia})\mathscr F_N(k-a)/\mathscr F_N(k)\);
the negative derivative in (8) is canceled by the minus sign when
the moving residues are moved to the right side of the residue
theorem. The \(k=0\) amplitude includes \(G_N(r)/(r^N-1)\).
Cancel it as \(-1/(1-r)\). Finally use
\[
 (1-e^{-2\pi ia})\mathscr F_N(-a)=\mathscr F_N(N-a),
 \quad
 \mathscr F_N(N-a)\mathscr F_N(a-1)
                     =Nq^{(N-a)(1-a)}
 \tag{29}
\]
to get the pole-free last line of (28). Thus (27)--(28) continue
through every positive integer \(a\) and through \(r^N=1\), with the actual whole
source, not a value-only cancellation. At \(a=1\), \(R_0=1\)
and every \(R_k\), \(k>0\), vanishes, while
\(\mathcal G_a/\mathcal G_1=1\). This is precisely the original
three-input geometric residue. Collisions with old outer families
are covered by the exact canceled expression (26).

## 5. The strict connector gap

Set
\[
 \begin{split}
 h_0&=\mathcal L(S)-\mathcal L(b)-\mathcal L(c)>0,\\
 P(v)&=\mathcal L(v)+\mathcal L(v-S)+\mathcal L(S)
       -\mathcal L(b)-\mathcal L(c)
       -\mathcal L(v-b)-\mathcal L(v-c),\\
                         M&=P(u),\qquad u=1-R .
 \end{split}
 \tag{30}
\]
These are the rates of the explicit factorials above. Uniformly
on compact sets,
\[
                         M-h_0\ge\delta>0 .
 \tag{31}
\]
Here is a direct verification. For \(x,y>0,x+y<1\),
\(\mathcal L(x+y)-\mathcal L(x)-\mathcal L(y)>0\).
Its derivative in \(x\) is
\(\log[\sin\pi(x+y)/\sin\pi x]\); it has one maximum,
zero limits at the two ends, and is positive between them.
This proves \(h_0>0\).

On \((\max(b,c),S)\), \(P'\) is the logarithm of
\[
 \left|\frac{(1-v_0)(1-yzv_0)}
                   {(1+yv_0)(1+zv_0)}\right|,
                         \qquad v_0=e^{2\pi iv}.
 \tag{32}
\]
The numerator of its squared modulus minus one is
\[
 16\sin(\pi b)\sin(\pi c)
       [\cos(2\pi v-\pi S)-\cos(\pi b)\cos(\pi c)].
\]
If \(\omega=\pi^{-1}\arccos(\cos\pi b\cos\pi c)\), then
\(|b-c|<\omega<S\). Its two crossings
\((S-\omega)/2,(S+\omega)/2\) therefore lie respectively
below \(\min(b,c)\) and strictly between \(\max(b,c)\) and
\(S\). This gives one maximum and no interior minimum for \(P\)
on the interval in question.
Also \(P(S)=2h_0\). If \(b\ge c\),
\[
 P(b)-h_0=\mathcal L(b)-\mathcal L(c)-\mathcal L(b-c)\ge0,
 \tag{33}
\]
with equality only at \(b=c\). In that case \(P\) increases
strictly immediately to the right of the endpoint. Thus \(P>h_0\)
throughout the open interval; compactness proves (31).

For later contour bounds, put
\[
 \mathcal R(v)=\frac{(1-v)(1-yzv)}{(1+yv)(1+zv)},\qquad
                       \chi=-\mathcal R(r)>0 .
 \tag{34}
\]
For \(v=re^{-2\pi Y}\), set \(w=ve^{-\pi iS}\),
\(s_0=2\cos\pi(b-c)>t_0=2\cos\pi S\).
Since \(\arg(re^{-\pi iS})=\pi(2u-S)\in(0,\pi)\),
\[
 \mathcal R(v)=\frac{1-t_0w+w^2}{1-s_0w+w^2},\quad
 \Im\mathcal R(v)=
 \frac{(s_0-t_0)(1-|w|^2)\Im w}{|1-s_0w+w^2|^2}.
 \tag{35}
\]
Thus its argument continued from \(\pi\) at \(Y=0\) lies
in \((0,\pi)\) above, and \((\pi,2\pi)\) below.

Let \(\mathcal V(Y)\) be the real rate, normalized to zero at
zero, of
\[
 \frac{\mathscr F_N(Nu+iNY)\mathscr F_N(N(u+1-S)+iNY)}
 {\mathscr F_N(N(u-b)+iNY)\mathscr F_N(N(u-c)+iNY)}
\]
including the rate \(2\pi Y\) for \(Y<0\) of the one-sided
Barnes kernel. Its derivative is \(-\arg\mathcal R(v)\) for
\(Y>0\), and \(2\pi-\arg\mathcal R(v)\) for \(Y<0\).
Consequently its unique maximum is zero, its one-sided slopes
there are \(-\pi,+\pi\), and
\[
 \sup_{|Y|\ge\epsilon}\mathcal V(Y)\le-\delta_\epsilon<0,
 \qquad
 \lim_{Y\to\pm\infty}\mathcal V(Y)=h_0-M .
 \tag{36}
\]
The limits follow from (9): the real part of the upper constant
of \(f\), and of its lower constant after subtracting
\(i\pi(w^2-w)\), is zero. They can also be read off the
normalized dilogarithm primitive. All limits and losses are uniform.

## 6. An exact finite Barnes identity without pinched integer parameters

Fix an integer \(\ell\ge a_+\). For \(0\le k\le\ell\),
the finite products in (28) give, uniformly even at their integer zeros,
\[
 R_k=r_k+O(N^{-1}),\qquad
 r_k=\frac{(1-a)_k(-\chi)^k}{k!}
                         =\binom{a-1}{k}\chi^k .
 \tag{37}
\]
Here \((1-a)_k\) is the ordinary rising factorial.
Remove the first \(\ell\) terms before deforming the packet. Define
\[
 \begin{split}
 T_N(v)={}&Q^v
 \frac{\mathscr F_N(v+\ell-a)\mathscr F_N(\ell)}
      {\mathscr F_N(\ell-a)\mathscr F_N(v+\ell)}\\
 &\times
 \frac{\mathscr F_N(L+a+\ell-1+v)\mathscr F_N(L+C+\ell+v)}
      {\mathscr F_N(L+a+\ell-1)\mathscr F_N(L+C+\ell)}\\
 &\times
 \frac{\mathscr F_N(D_y+\ell)\mathscr F_N(D_z+\ell)}
      {\mathscr F_N(D_y+\ell+v)\mathscr F_N(D_z+\ell+v)} .
 \end{split}
 \tag{38}
\]
The finite product identity is \(R_{k+\ell}=R_\ell T_N(k)\).
The explicit right side (38) stays regular when \(R_\ell=0\);
no division by that coefficient defines the interpolation.
Use left line \(\Re v=\gamma=-1/4\), right line
\(\Re v=\beta=p+\zeta-\ell\), and kernel
\[
                         \mathcal B(v)=\frac{2\pi i}{e^{2\pi iv}-1}.
 \tag{39}
\]
The only poles in this rectangle are the integer samples
\(0,\ldots,K-\ell\). In particular, the negative poles of
\(\mathscr F_N(v+\ell-a)\) are at \(v=a-\ell-1-m\), all to the
left. The denominator arguments in (38) stay within their
zero-free first strips; no hidden outer family is crossed.

Horizontal sides vanish at fixed \(N\). The total factorial
shift difference in (38) is \(N-2\). Below, including \(Q^v\)
and (39), the net decay is \(e^{-2\pi|\Im v|/N}\);
above it is the same. Therefore, with both integrals upward,
\[
 S_{N,a}=\sum_{k=0}^{\ell-1}R_k+
                         R_\ell(J_{\rm right}-J_{\rm left}),\qquad
 J_{\rm line}=\frac1{2\pi i}\int_{\rm line}\mathcal B(v)T_N(v)\,dv .
 \tag{40}
\]
This is finite, and retains the right connector explicitly.

## 7. Central estimate, macroscopic tails, and right connector

On the left line, uniformly for \(|\Im v|\le\epsilon N\),
(10)--(13) give
\[
 T_N(v)=e^{i\pi v}\chi^v
       \frac{\Gamma(v+\ell+1-a)\Gamma(\ell+1)}
            {\Gamma(\ell+1-a)\Gamma(v+\ell+1)}
          \exp\{O((1+|v|)^2/N)\}.
 \tag{41}
\]
The logarithm of \(\mathcal R(r)\) here is \(i\pi+\log\chi\),
fixed by the canonical factorials. The model Barnes integrand has
bound \(C(1+|\Im v|)^C e^{-\pi|\Im v|}\).
Choose \(\epsilon\) small enough that the error exponential in
(41) is absorbed by half of this decay. Its integrated error is
then \(O(N^{-1})\), by
\[
 \frac C N\int_{\mathbb R}(1+|T|)^C e^{-\pi|T|/2}\,dT .
 \tag{42}
\]

Here are quantitative majorants for both remaining infinite pieces.
For \(v=\gamma+iNY,\ |Y|\ge\epsilon\), the exact bounds
(10)--(11), with the continued endpoint branches, give
\[
 |\mathcal B(v)T_N(v)|
       \le C N^C e^{N\mathcal V(Y)}e^{-\pi|Y|}.
 \tag{43}
\]
To verify the integrable last factor, the fixed-shift amplitude
of the two macroscopic numerator factors relative to the two
denominators is \(e^{2\pi(a-2)|Y|}\) below. The light
factorial ratio supplies \(e^{-2\pi a|Y|}\), and \(Q^v\)
supplies \(e^{2\pi|Y|}\). The Barnes kernel's exponential
\(e^{-2\pi N|Y|}\) is already in \(\mathcal V\).
Their remaining product is exactly \(e^{-2\pi|Y|}\).
Above only \(Q^v\) has a nonconstant limiting modulus and gives
the same decay. Full-strip Stirling errors are uniformly bounded.
Replacing \(2\pi\) by \(\pi\) absorbs bounded-height transitions,
uniformly for the bounded shifts and angles. This proves (43)
with an integrable majorant after the \(N^C\) factor.
Equations (36), (43) bound this left tail by
\(C N^C e^{-\delta_\epsilon N}\).

On the right line, write \(v=p+\zeta-\ell+iNY\). The two numerator
arguments in (38) become \(N+a+\zeta-1+iNY\) and
\(N+C+\zeta+iNY\). Apply (7) once to each. They contribute
two periodic numerator factors. The denominator arguments are
\(N(1-b)+\zeta+1/2+iNY\) and its \(c\)-analogue.
Let \(R_0\) be the rate in the proof of (22). The resulting rates,
including (39) and normalization by the central factorials, are
\[
 \mathcal W(Y)=
 \begin{cases}
 R_0(Y)-M,&Y\ge0,\\
 R_0(Y)-2\pi Y-M,&Y\le0 .
 \end{cases}
 \tag{44}
\]
The argument computation in (23) gives
\[
 R_0'(Y)=T(Y)\quad(Y>0),\qquad
 R_0'(Y)=\pi+T(Y)\quad(Y<0),\qquad 0<T(Y)<\pi.
 \tag{45}
\]
Both \(R_0(Y)\) above and \(R_0(Y)-2\pi Y\) below increase
toward the same end value \(h_0\), when moving away from zero.
Consequently \(\mathcal W(Y)\le h_0-M\le-\delta\).

The fixed-shift amplitude count on this line is again
\(e^{2\pi(a-2)|Y|}\), from the two shifted numerators and
denominators; the light ratio and \(Q^v\) complete it to
\(e^{-2\pi|Y|}\). Its two periodic factors, with the Barnes
kernel, supply exactly the macroscopic correction in (44).
For \(|Y|\ge\epsilon\), (10)--(11) therefore give
\[
 |\mathcal B(v)T_N(v)|
             \le C N^C e^{-N(M-h_0)}e^{-\pi|Y|}.
 \tag{46}
\]
For \(|Y|\le\epsilon\), the sole endpoint numerator has bounded
real shift greater than \(-1\). Its Gamma product, or comparison
with the exact half-step formula [P, equation (35)], costs at most
\(N^C(1+N|Y|)^C e^{C|Y|}\). The remaining factors use
(10). Their rate is still (44). Thus this finite interval is
bounded by \(C N^C e^{-N(M-h_0)}\) after increasing the
polynomial power. Integration, with \(dv=iN\,dY\), proves
\[
                         |J_{\rm right}|
                    \le C N^C e^{-\delta N}.
 \tag{47}
\]
The connector is exponentially negligible relative to the central
packet, even though it need not be polynomial before normalization.

The model left integral is elementary. Using
\(\Gamma(-v)\Gamma(v+1)=-\pi/\sin\pi v\), (41) gives
\[
 -J_{\rm left}=
 \frac1{2\pi i}\int_{\gamma-i\infty}^{\gamma+i\infty}
 \frac{\Gamma(-v)\Gamma(v+\ell+1-a)\Gamma(\ell+1)\Gamma(v+1)}
      {\Gamma(\ell+1-a)\Gamma(v+\ell+1)}
                         \,\chi^v\,dv+O(N^{-1})
 =\ell\int_0^1(1-x)^{\ell-1}(1+\chi x)^{a-\ell-1}\,dx
                                      +O(N^{-1}).
 \tag{48}
\]
For a direct proof of the last equality, first close the ordinary
Gamma Barnes contour at \(|\chi x|<1\) and sum its binomial
residues; the exponentially convergent vertical integral continues
this identity to positive \(\chi x\). Integrating in \(x\)
is justified by \(\gamma>-1\). The Gamma parameter
\(\ell+1-a\) is at least one. Thus there is no restriction
\(\chi<1\), and the same contour works through every integer \(a\).

Taylor's integral remainder gives the exact model identity
\[
 \sum_{k=0}^{\ell-1}r_k+
 r_\ell\ell\int_0^1(1-x)^{\ell-1}(1+\chi x)^{a-\ell-1}\,dx
                                      =(1+\chi)^{a-1}.
\]
Combining this with (37), (40), (47)--(48) proves
\[
                         S_{N,a}=(1+\chi)^{a-1}(1+O(N^{-1})).
 \tag{49}
\]
The model is positive and bounded away from zero uniformly on our
compact parameters. At \(a=1\), (49) is the exact identity
\(S_{N,1}=1\).

## 8. Prefactor, source-relative error, and scope

The pole-free ratio (28) and (10), (12) give
\[
 \frac{\mathcal G_a}{\mathcal G_1}
  =\frac{N^{2a-2}}{\Gamma(a)^2}
                \left(\frac{\sin\pi R}{\pi}\right)^{2a-2}
                       (1+O(N^{-1})).
 \tag{50}
\]
To check its phase, the two macroscopic ratios give
\((1-r^{-1})^a(1-r)^{a-1}\); the small factorial is
\((-2\pi i/N)^{a-1}\Gamma(a)(1+O(N^{-1}))\).
Use the canonical arguments
\(\arg(1-r)=\pi u-\pi/2\),
\(\arg(1-r^{-1})=-\arg(1-r)\), and
\(-r(1-r^{-1})/(1-r)=1\).
The phase of \(q^{(N-a)(1-a)}\) cancels the remaining
endpoint phase. This gives the positive factor in (50), not just
its modulus.

By (10) and (30), \(|\mathcal G_1|\ge N^{-C}e^{NM}\).
Equations (22), (27), (49)--(50), with \(M>h_0>0\), now
control the error relative to the actual geometric source.
In particular \(\Phi_1/\mathcal G_1=1+O(N^Ce^{-NM})\).
Finally
\[
 1+\chi=\frac{\sin\pi b\sin\pi c}
                  {\sin\pi(u-b)\sin\pi(u-c)}
 \tag{51}
\]
follows directly from (34). Equations (49)--(51) prove (5).
No estimate of a weighted signed sum has been substituted for the
retained packet/current decomposition.

This theorem supplies only the displayed small-angle boundary data.
It does not itself propagate a generic offset to a fixed positive
boundary angle, cross a fold, initialize another prism face, or
control an arbitrary attached short component. No knot-volume or
finite-exception conclusion is asserted.

The complete direct proof sources are:

| Label | Complete source | SHA-256 |
|---|---|---|
| B | notes/research_four_coherent_boundary_polynomial_source.md | 93241074830ff4b844ba5baafd06a15bf08ec6bddc3a1498727f110ebe297d84 |
| P | notes/research_centered_tensor_full_prism_source_transport.md | eb43e287eca5933b70de3b6362a81f92d46bb2e121f0eb5716793c107adaef10 |

Both entire matching proof texts were read. Only written mathematics
and text reads, edits and hashes were used. No mathematical programs,
tests, numerical experiments, builds or git operations were run.
This research proof is author-final.
