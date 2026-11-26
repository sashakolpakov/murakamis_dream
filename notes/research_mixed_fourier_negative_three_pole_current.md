# The complete three-negative-crossing pole and endpoint current

Research deduction, 7 November 2026. The complete source after three
negative crossings is a canonical pole product plus one explicit
infinite endpoint current. Both horizontal contour terms vanish.
The full current has a uniform absolute bound at the original
last-row forcing rate. The pole product has a nonzero packet and
lies strictly below that rate on the original incoming plateau.
Consequently the entire crossed source, rather than only its first
coefficient, is exponentially smaller than the original cap there.

This comparison is to the original cap action. It does not show that
the pole product leads the crossed source: the signed endpoint
current has not been compared to the smaller pole action.
No numerical evaluation or new source certificate is used.

## 1. The exact residue decomposition

Use \(N,D,q,r,\kappa,P_j,X=e^{-2\pi ia},Y=e^{2\pi iy}\) and
\(G_{-3}=\mathcal M_{-3}Z_N\) from
[the complete three-negative-crossing source](research_mixed_fourier_negative_three_full_source.md).
First let the parameters range in a fixed compact subset of
\[
 0<\Re a<1/2,\qquad 0<\Re y<1/2,\qquad \Im y>0.
\tag{1}
\]
The canonical factorial and reciprocal are the original
\(\Pi_N,E_N\), with the holomorphic continuations of
[the global joint chart](research_mixed_fourier_right_cap_joint_global_chart.md).
Put
\[
 \begin{split}
 R_N(s;a)&=e^{2\pi iNas}\Pi_N(s+a)E_N(a)E_N(s),\\
 F_N(s;a,y)&=\frac{R_N(s;a)}
                    {1-Y^{-1}r e^{-2\pi is}},\\
 \alpha_N&=-\frac1{2N},\qquad \beta_N=\alpha_N+1,\qquad
 s_0=1-y-\frac1N .
 \end{split}
\tag{2}
\]
On the complete half-grid strip, \(R_N\) is holomorphic; positive
numerator walls are zeros. The only pole of \(F_N\) in that strip
is \(s_0\), and
\[
 \operatorname{Res}_{s=s_0}F_N(s)=\frac{R_N(s_0;a)}{2\pi i}.
\tag{3}
\]
At physical indices \(R_N(j/N;a)=X^{-j}(rX;r)_j/P_j\).
Thus the exact rational sum is
\[
 G_{-3}(a,y)=
 \frac{\kappa^{-3}e^{\pi iDy}}{N^2}(1-Y^{-N})
                    \sum_{j=0}^{D}F_N(j/N;a,y).
\tag{4}
\]

Use the upper-side kernel
\[
 K_N^+(s)=\frac{N}{e^{2\pi iNs}-1}.
\tag{5}
\]
Its residue at each physical node is \(1/(2\pi i)\), while
\[
             K_N^+(s_0)=\frac{NY^N}{1-Y^N}.
\]
The original exact cyclotomic factorial asymptotics give, at fixed
\(N\), uniformly in bounded real strips,
\[
 \begin{split}
 R_N(s;a)&=E_N(a)e^{2\pi iNas}(1+o(1)),
                                      &&\Im s\longrightarrow-\infty,\\
 R_N(s;a)&=D_N(a)(1+o(1)),
                                      &&\Im s\longrightarrow+\infty,\\
 D_N(a)&=E_N(a)
             e^{i\pi\{N(a-a^2)-a\}} .
 \end{split}
\tag{6}
\]
These follow by applying the reflected factorial formula to
\(\Pi_N(s+a)/\Pi_N(s)\); the two \(s\)-linear terms cancel
the original chirp exactly. The specified Gamma-product constants
cancel as well. The lower horizontal integral of \(K_N^+F_N\)
decays at rate \(e^{-2\pi N(1-\Re a)H}\). On the upper line,
the rational denominator gives the additional factor
\(e^{-2\pi H}\), while \(K_N^+\) tends to \(-N\).
Both horizontal integrals therefore vanish with \(N\) fixed.

For the vertical sides write
\[
 A=X^N,\qquad t=e^{-2\pi iNs}.
\]
The exact one-period factorial relation gives
\[
 \frac{R_N(s+1;a)}{R_N(s;a)}
       =\frac{1-At}{A(1-t)},\qquad
 F_N(s+1)-F_N(s)=\frac{1-A}{A(1-t)}F_N(s).
\tag{7}
\]
These may equally be used as undivided identities at zeros.
At \(s=\alpha_N+iv\), put \(T=e^{2\pi Nv}\); then
\(t=-T\) and \(K_N^+=-NT/(1+T)\).
Taking the counterclockwise residue identity to infinite height
therefore proves
\[
 \boxed{\quad G_{-3}(a,y)=\mathcal P_{-3,N}(a,y)
                                  +\mathcal J_{-3,N}(a,y),\quad}
\tag{8}
\]
where
\[
 \boxed{\quad
 \mathcal P_{-3,N}(a,y)
       =\frac{\kappa^{-3}e^{\pi iDy}}N R_N(s_0;a),
 \quad}
\tag{9}
\]
\[
 \boxed{\quad
 \mathcal J_{-3,N}
   =-\frac{i\kappa^{-3}e^{\pi iDy}}N
        (1-Y^{-N})\frac{1-X^N}{X^N}
       \int_{\mathbb R}
       \frac{T}{(1+T)^2}F_N(\alpha_N+iv;a,y)\,dv .
 \quad}
\tag{10}
\]
The sign in (9) uses
\((1-Y^{-N})Y^N/(1-Y^N)=-1\) and the subtraction of
the additional pole from the node sum. In (10) the right boundary
is traversed upward. These fix both signs without resetting a
periodic branch.

At \(a=b/N\), the current vanishes exactly and the pole product is
\[
 R_N(s_0;b/N)=\frac{(r/Y)^b(Y;r)_b}{P_b}.
\tag{11}
\]
This is the same physical product as in the preceding source note,
now tied to its actual index pole. Equations (8)--(10), rather
than agreement at nodes alone, specify its off-grid correction.

## 2. A uniform bound for the full infinite current

Write \(x=\Re a,\ h=\Im a,\ \xi=\Re y,\ \upsilon=\Im y\).
For real \(v\) define the original regular-strip profile
\[
 L_a(v)=\Re\{g(a+iv)-g(a)\}-2\pi xv,\qquad L_a(0)=0.
\tag{12}
\]
On \(0<x<1/2\), the original logarithm has
\[
 0<\Im g'(x+iH)<\pi-2\pi x
 \quad\hbox{at every real }H.
\]
Indeed \(1-Re^{-2\pi ix}\), \(R>0\), remains in the upper
half-plane with argument between these two limiting angles.
Consequently
\[
                       -\pi<L_a'(v)<-2\pi x.
\tag{13}
\]

On any fixed bounded height interval, the regular numerator
packet, including its half-grid shift, and the exact midpoint
identity give
\[
 |\Pi_N(\alpha_N+iv)|^2=\frac{N}{1+T},\qquad
 |R_N(\alpha_N+iv;a)|
       \le \frac{C}{\sqrt N}\sqrt{1+T}\,e^{NL_a(v)}.
\tag{14}
\]
No endpoint Stirling approximation replaces the first identity.
The remaining Cauchy denominator is uniformly bounded away from
zero, at every height. In fact it is
\[
 1-e^{2\pi(v+\upsilon)}e^{-i(2\pi\xi+\pi/N)},
\]
and the elementary inequality
\[
 |1-z e^{-i\theta}|\ge
             |\sin(\theta/2)|(1+z),\qquad z\ge0,
\tag{15}
\]
applies. On compact parameter sets in (1), its sine factor has
a common positive lower bound for all \(N\ge2\).

After multiplication by \(T/(1+T)^2\), the exponential rate in
(14) is bounded by
\[
 \mathcal L_a(v)=
 \begin{cases}
 L_a(v)+2\pi v,&v\le0,\\
 L_a(v)-\pi v,&v\ge0 .
 \end{cases}
 \qquad
             \mathcal L_a(v)\le-\pi|v|.
\tag{16}
\]
This follows directly from (13), with value zero at the seam.
Thus the integral over any fixed compact height interval is
at most \(CN^{-3/2}\).

For completeness this bound extends to both unbounded tails
uniformly in \(N\), not merely by fixed-level convergence.
Use the explicit remainder of
[the cyclotomic factorial formula](research_exact_cyclotomic_factorial.md),
equations (8)--(9). If \(H_0\) bounds the parameter heights,
one may bound each normalized remainder at height \(v\ge H>H_0+1\)
by a positive function
\[
 \epsilon(v)=
 \frac{(v+C_0+1)\rho_v^2}{2(1-\rho_v^2)}
                 +\frac{\rho_v}{2(1-\rho_v)},\qquad
 \rho_v=e^{-2\pi(v-H_0)},
\tag{17}
\]
where \(C_0\) bounds the fixed real parts and shifts.
Its tail supremum \(\epsilon_H\) tends to zero as \(H\) grows.
The two varying factorial remainders at each end of a ratio
cost at most \(4N\epsilon_H\).

Let
\[
 Q_N(v)=\frac{e^{2\pi Nv}}{(1+e^{2\pi Nv})^2}
                         F_N(\alpha_N+iv).
\]
For a sufficiently large fixed \(H\), (6) and the exact kernel
and Cauchy denominator imply, for \(v\ge H\),
\[
 \begin{split}
 |Q_N(v)|&\le C|Q_N(H)|
             e^{-2\pi(N+1)(v-H)+4N\epsilon_H},\\
 |Q_N(-v)|&\le C|Q_N(-H)|
             e^{-2\pi N(1-x)(v-H)+4N\epsilon_H}.
 \end{split}
\tag{18}
\]
The extra \(+1\) in the first line comes from the Cauchy
denominator, not a large-\(N\) phase approximation.
Only the left-side factors are divided in this ratio:
their factorials and Cauchy denominator are zero-free there.
For example at large positive height the denominator ratio is
at most \(4e^{-2\pi(v-H)}\); at negative height it is bounded
by a constant. The kernel ratios contribute
\(4e^{-2\pi N(v-H)}\) in either direction.

Choose \(H\) once so that \(4\epsilon_H<\pi H/2\).
The value at either starting height is bounded by
\(CN^{-1/2}e^{-\pi NH}\), by (14)--(16).
Integrating (18) then has the same \(N^{-3/2}\) cost as the
compact interval. This proves absolute convergence and
\[
 \left|\int_{\mathbb R}Q_N(v)\,dv\right|
 \le \int_{\mathbb R}|Q_N(v)|\,dv\le CN^{-3/2}.
\tag{19}
\]
Keeping all exact period factors in (10) yields
\[
 \boxed{\quad
 |\mathcal J_{-3,N}(a,y)|
       \le CN^{-5/2}
           e^{N e_{\rm end}(a,y)},\qquad
 e_{\rm end}(a,y)=2\pi(-h)_++\pi\upsilon .
 \quad}
\tag{20}
\]
Here \(|(1-X^N)/X^N|\le2e^{2\pi N(-h)_+}\) and
\(|1-Y^{-N}|\le2e^{2\pi N\upsilon}\); the bounded factor
\(e^{\pi\upsilon}\) is included in \(C\).
The signed current may be much smaller than (20).

## 3. The pole packet and its original-action comparison

Assume in addition
\[
                    0<\xi<x<1/2,\qquad h<\upsilon.
\tag{21}
\]
Then \(a-y\) and \(-y\) are in the original lower half-plane.
The uniform lower-half factorial packet and the regular packet
at \(a\) show
\[
 \mathcal P_{-3,N}(a,y)
     =\kappa^{-3}N^{-3/2}\mathcal A_p(a,y)
                       e^{N\Phi_p(a,y)}(1+O(N^{-1})),
\tag{22}
\]
where
\[
 \begin{split}
 \Phi_p(a,y)&=\pi iy+g(a-y)-g(a)-g(-y)+2\pi ia(1-y),\\
 \mathcal A_p(a,y)&=
    e^{-\pi iy}\frac{X(1-Y)}{1-XY}
       \frac{\mathfrak a(a-y)}
            {\mathfrak a(a)\mathfrak a(-y)} .
 \end{split}
\tag{23}
\]
Here \(\mathfrak a\) is the original nonzero factorial symbol,
with its continued lower-half branch where needed. This notation
distinguishes the symbol from the incoming parameter \(a\).
All factors in \(\mathcal A_p\) are nonzero under (21).
The shift \(-1/N\) in \(s_0\) contributes
\(e^{-2\pi ia-g'(a-y)+g'(-y)}=X(1-Y)/(1-XY)\).
The lower-half primitive and symbol are one-periodic, so the
shifted numerator \(s_0+a\) is treated on its original continued
branch, not by discarding a positive-wall factor on the real line.

We next compare this pole action to the already proved endpoint
rate, not to a conjectured crossed action.
For \(0<x<1/2\), let \(J(x)=\Re g(x)\). Its minimum is at
\(1/6\), and
\[
                    -J(x)<\frac16 .
\]
An elementary proof is \(2\sin(\pi t)>6t\) on \(0<t<1/6\),
followed by integration; \(J'(x)=\log(2\sin\pi x)\)
locates the minimum. The same argument bounds every other
point in the half-period. The all-height argument bound gives
\[
                 -\Re g(a)<\frac16+\pi(1-2x)h_+ .
\tag{24}
\]
Moreover
\[
                   \Re g(a-y)<0<\Re g(-y).
\tag{25}
\]
To see the signs without a series estimate, radially differentiate
the imaginary part of the dilogarithm. Its derivative is
\(-\arg(1-Re^{i\theta})/R\), whose sign is fixed for
\(0<|\theta|<\pi\), and its value at \(R=0\) is zero.

Subtracting \(e_{\rm end}\) from (23), using (24)--(25),
therefore gives
\[
 \Re\Phi_p-e_{\rm end}
 <\frac16-2\pi\upsilon(1-x)+
 \begin{cases}
 2\pi h\xi,&h\le0,\\
 -\pi h(1+2x-2\xi),&h\ge0.
 \end{cases}
\tag{26}
\]
Both additional terms are nonpositive.
For the original output \(y=x_0\), on the whole original
incoming plateau \(x\in[11/50,9/20]\) and all its admitted
actual reference heights, (21) holds. In particular
\(h\le17/250<\upsilon\), \(x>\xi\), and
\(\upsilon>157/2000\). The inherited bounds and \(\pi>3\)
give
\[
 2\pi\upsilon(1-x)>
       6\,\frac{157}{2000}\frac{11}{20}
       =\frac{5181}{20000},\qquad
 \boxed{\quad
   \Re\Phi_p-e_{\rm end}<-\frac{5543}{60000}<-\frac1{12}.
 \quad}
\tag{27}
\]
This proof does not require a new critical point or a numerical
action comparison.

## 4. The whole crossed source is paid relative to the original cap

Fix an actual reference \(a_*\in K_{3+\eta}\), \(\eta=0,1\),
its original incoming height \(h=\Im a_*\), and \(y=x_0\).
For \(a=x+ih,\ x\in P=[11/50,9/20]\), retain the original
allocated cap plane \(B_\eta(x)\).
The completed
[endpoint payment](research_mixed_fourier_right_cap_endpoint_payment.md)
states
\[
 e_{\rm end}(a,x_0)-\frac{\eta}{2}\Re g(a)
           <B_\eta(x)-\frac{387}{70000}.
\tag{28}
\]
Equations (8), (20), (22), and (27) bound the complete
\(G_{-3}\) by \(CN^{-5/2}e^{N e_{\rm end}}\) for large \(N\).
For \(\eta=1\), apply only the original admitted negative-height
upper estimate for the finite Fourier weight; never divide it
out on the target plateau. With an arbitrary sufficiently small
fixed rate tolerance, (28) proves
\[
 \boxed{\quad
 |d_N(e^{-2\pi ia})|^{\eta/2}
        |\mathcal M_{-3}Z_N(a,x_0)|
       \le e^{N\{B_\eta(x)-1/200\}}
 \quad}
\tag{29}
\]
for all sufficiently large levels of both parities.
Every original finite channel and numerator zero is still present.

There is also a local holomorphic consequence for the whole source.
At \((a_*,x_0)\), the incoming allocation cancels in (28)
against the original cap phase \(\Phi\). The continuous endpoint
rate, the strict pole comparison, and the compact-uniform bounds
above preserve a gap strictly larger than \(1/200\) on a small
complex neighborhood. The original
[holomorphic cap packet](research_mixed_fourier_right_cap_holomorphic_packet.md)
is nonzero there for all sufficiently large \(N\).
Thus, on a smaller neighborhood and for every fixed multi-index
\(\alpha\),
\[
 \boxed{\quad
 \left|\partial^\alpha
       \frac{\mathcal M_{-3}Z_N(a,y)}{Z_N(a,y)}\right|
       \le C_\alpha e^{-N/200}.
 \quad}
\tag{30}
\]
This follows by the uniform unallocated bounds and nested Cauchy
estimates, rather than division by a finite incoming weight.

Equations (29)--(30) compare the entire crossed function to the
original cap. They do not compare \(\mathcal J_{-3,N}\) to the
nonzero pole packet (22). The exact midpoint layer retains the
oscillation of the original Gamma factor, so its absolute forcing
rate is not asserted to be its true exponent. A proof that the
pole leads would require a sharper signed-current estimate at
\(\Re\Phi_p\), or an equivalent connection argument for the exact
forced difference relation. That question remains open here.
