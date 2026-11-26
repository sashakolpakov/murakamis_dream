# The first-unselected main profiles on the positive second shoulder

Private written proof, 11 November 2026. This note pays the two ordinary
main profiles at the positive second shoulder of an actual word beginning
with \(444\). It uses the original common central reserve \(1/3200\),
including when the following external leg has type three. The first
coordinate is unselected. No double-selected reserve is used.

The conclusion is a profile comparison, with the complete cap allocation
attached in Section 6. Ordinary complementary currents, the complete
first-period polynomial on this shoulder, and a complete second period
are not asserted.

## 1. Original source and comparison

Fix an actual positive three/four word of length \(m\ge4\) beginning with
\(444\), retaining its original critical reference and logarithmic lifts.
Write
\[
 \begin{gathered}
 a_*=r_1,\quad s_*=s_2^*,\quad y_*=r_2,\quad
 t_*=s_3^*,\quad z_*=r_3,\\
 c_1=\Im a_*,\quad h_2=\Im s_*,\quad h_3=\Im t_*,
 \quad c_3=\Im z_*,\\
 -.078<c_1<-.020,\qquad -.102<h_2,h_3,c_3<-.001.
 \end{gathered}
 \tag{1}
\]
These are necessary bounds on the actual coupled reference from the
[reference-curve theorem](research_mixed_second_selected_reference_curve.md),
not an independent box reference. The following external leg is attached
at \(m=4\), ordinary thereafter, and stays in the original \(K_3\cup K_4\).

Set \(P=[11/50,9/20]\), \(H=1/100\), and
\[
 a=x+ic_1,\quad z=b+ic_3,\quad x,b\in P,\qquad
 y=q+iH,\quad 9/20\le q\le1/2.
 \tag{2}
\]
Fix \(r_0\in(1/4,1/2)\). The two ordinary main indices range over
\([1/8,r_0]+ih_2\) and \([1/8,r_0]+ih_3\). Every shifted argument
then stays strictly inside the original regular strip, including at
\(q=1/2\). Use exactly
\[
 \begin{split}
 g(w)&=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},\\
 Q(s;a,y)&=g(s+a)+g(s+y)-3g(s)-g(a)-g(y)+2\pi ias,\\
 M_2(q)&=\max_{1/8\le u\le r_0}\Re Q(u+ih_2;a,y),\\
 M_3(q)&=\max_{1/8\le v\le r_0}\Re Q(v+ih_3;y,z).
 \end{split}
 \tag{3}
\]
The chirps are retained. The two full selected second-weight rates are
\[
 W^{\rm fac}(y)=-\Re g(y)-2\pi H,\qquad
 W^{\rm force}(y)=0.
 \tag{4}
\]
They belong to the original \(d_N(Y)Y^{-N}\), not to a halfweight.

The original allocated reference phase and affine bound are
\[
 \begin{split}
 F_{23}(a,s,y,t,z)&=Q(s;a,y)+Q(t;y,z)
                    -g(y)-\tfrac12g(a)-\tfrac12g(z),\\
 \Lambda_{23}(a,z)&=
 \Re\{F_{23,*}+p_L(a-a_*)+p_R(z-z_*)\},
 \end{split}
 \tag{5}
\]
where \(p_L,p_R\) are its original complex boundary derivatives.
The latter is independent of the target \(q\). The
[central completion](research_mixed_second_selected_central_completion.md),
Theorem 1, gives at \(q=9/20\), for both alternatives,
\[
 M_2+M_3+W^\nu(y)-\tfrac12\Re g(a)-\tfrac12\Re g(z)
       <\Lambda_{23}(a,z)-\frac1{3200}.
 \tag{6}
\]
That source bounds the larger private intervals up to \(1/2\).

**Proposition.** Throughout (1)--(2), for either alternative in (4),
\[
 M_2(q)+M_3(q)+W^\nu(y)
       -\tfrac12\Re g(a)-\tfrac12\Re g(z)
 \le \Lambda_{23}(a,z)-\frac1{72000}.
 \tag{7}
\]
The constant is independent of the fixed choice \(r_0\in(1/4,1/2)\).
No ratio between the reference shapes \(e^{-2\pi is_*}\) and
\(e^{-2\pi it_*}\) is assumed.

## 2. Height constants

Put
\[
 r=e^{\pi/50},\quad \rho_j=e^{2\pi h_j},\quad
 T_a=e^{-2\pi c_1},\quad R_z=e^{2\pi c_3}.
 \tag{8}
\]
Then
\[
 \frac{17}{16}<r<\frac{16}{15},\quad
 \frac12<\rho_2,\rho_3<1,\quad T_a>\frac98,\quad
 R_z>\frac{13}{25},\quad \rho_3^{-1}<\frac{19}{10}.
 \tag{9}
\]
The first and third bounds follow from \(e^u>1+u\), \(\pi>25/8\),
and \(\log(16/15)>2/31>\pi/50\). The lower radii follow from
\(\log2>2/3>51\pi/250\). For the last two comparisons, the positive
series for \(2\operatorname{atanh}v\) gives
\[
 \log(25/13)>\frac{12}{19}+\frac{144}{6859}
       >\frac{619}{950}>\frac{561}{875}>\frac{51\pi}{250}.
 \tag{10}
\]
For \(v=9/29\),
\[
 \begin{split}
 \log(19/10)&>2v+\frac{2v^3}{3}+\frac{2v^5}{5},\\
 2v+\frac{2v^3}{3}&=\frac{15624}{24389}>\frac{1281}{2000},
 \qquad \frac{2v^5}{5}=\frac{118098}{102555745}>\frac1{1000}.
 \end{split}
 \tag{11}
\]
Their sum exceeds \(1283/2000>561/875\), proving (9).

## 3. The first main index passes \(7/10-q\)

For \(u\in[1/8,7/10-q]\), the shifted sums lie in
\([.345,.70]\) and \([.575,.70]\). Hence
\[
 \cos(2\pi(x+u)),\ \cos(2\pi(q+u))<-3/10,
 \tag{12}
\]
using \(\cos(2\pi/5)=(\sqrt5-1)/4>3/10\).
Also \(u\le1/4\), so the own denominator square is at most
\(1+\rho^2\), where \(\rho=\rho_2\).

The square of the force determining the real \(u\)-derivative is
\[
 \frac{|T_a-\rho e^{-2\pi i(x+u)}|^2
       |1-r\rho e^{-2\pi i(q+u)}|^2}
      {|1-\rho e^{-2\pi iu}|^6}.
 \tag{13}
\]
The factor \(T_a\) includes the original chirp. Its two numerator
squares exceed
\[
 A=\rho^2+\frac23\rho+\frac54,\qquad
 B=\frac98\rho^2+\frac58\rho+1.
 \tag{14}
\]
Expansion gives
\[
 \begin{split}
 AB-(1+\rho^2)^3={}&-\rho^6-\frac{15}{8}\rho^4
 +\frac{11}{8}\rho^3-\frac{17}{96}\rho^2
 +\frac{139}{96}\rho+\frac14\\
 &\ge\frac14-\frac5{96}\rho-\frac{17}{96}\rho^2
 \ge\frac1{48}\qquad(0\le\rho\le1).
 \end{split}
 \tag{15}
\]
Use \(\rho^6\le\rho^4\), \(\rho^3\ge\rho^4\), and
\(\rho^4\le\rho\) for the first inequality. Thus every first
maximizer satisfies \(q+u\ge7/10\). At every such maximizer,
\[
 N_2^2:=|1-r\rho_2e^{-2\pi i(q+u)}|^2
 \le A_f:=r^2+\frac58r+1.
 \tag{16}
\]
Indeed \(q+u<1\) and
\(-\cos(2\pi(q+u))\le\cos(2\pi/5)<5/16\), since \(\sqrt5<9/4\).

## 4. The second main index, split by its radius

Suppose first \(1/2\le\rho=\rho_3\le5/8\).
For \(v\in[1/8,69/100-q]\), the shifted sums lie in
\([.575,.69]\) and \([.345,.69]\), while \(v\le.24\).
Both shifted cosines are less than \(-11/30\), and the own cosine
is greater than \(1/16\). Explicit witnesses are
\[
 \begin{split}
 \sin(3\pi/25)&>
 \frac{471}{1250}-\frac{(19/50)^3}{6}
 =\frac{11}{30}+\frac{741}{750000},\\
 \sin(\pi/50)&>\frac{157}{2500}-\frac1{20250}>\frac1{16},
 \end{split}
 \tag{17}
\]
using \(157/50<\pi<22/7\) and \(\sin t\ge t-t^3/6\).

The force square for \(\Re Q(v+ih_3;y,z)\), after retaining its
chirp, has incoming numerator
\(|r^{-1}-\rho e^{-2\pi i(q+v)}|^2\), outgoing numerator
\(|1-R_z\rho e^{-2\pi i(b+v)}|^2\), and the own denominator
power in (13). The numerator squares exceed
\[
 A=\rho^2+\frac{11}{16}\rho+\frac78,\qquad
 B=\frac{27}{100}\rho^2+\frac{19}{50}\rho+1,
 \tag{18}
\]
while the own square is at most \(D=1+\rho^2-\rho/8\).
The polynomial \(P=AB-D^3\) is
\[
 P=-\rho^6+\frac38\rho^5-\frac{4443}{1600}\rho^4
 +\frac{3373}{2560}\rho^3-\frac{2479}{1600}\rho^2
 +\frac{279}{200}\rho-\frac18.
 \tag{19}
\]
On \([1/2,5/8]\),
\[
 \begin{split}
 P''&=-30\rho^4+\frac{15}{2}\rho^3
 -\frac{13329}{400}\rho^2+\frac{10119}{1280}\rho
 -\frac{2479}{800}\\
 &<8\rho^3-33\rho^2+8\rho-3<-4.
 \end{split}
 \tag{20}
\]
The last bound uses \(8\rho^3<2\), \(33\rho^2>8\), and
\(8\rho\le5\). The exact endpoint values are
\[
 P(1/2)=\frac{17653}{102400}>0,\qquad
 P(5/8)=\frac{2583}{163840}>0.
 \tag{21}
\]
Concavity proves \(P>0\), so every second maximizer in this radius
range has \(q+v\ge69/100\). Furthermore \(\sin t<t-t^3/7\)
for \(0<t<1\), and
\[
 \sin(3\pi/25)<\frac{151}{400}
      -\frac{(151/400)^3}{7}<\frac{37}{100}.
 \tag{22}
\]
The difference in the last comparison is
\(-82951/448000000\). Thus at every such maximizer,
\[
 N_3^2:=|\rho_3^{-1}-re^{-2\pi i(q+v)}|^2
 \le B_s:=r^2+\frac{703}{500}r+\frac{361}{100}.
 \tag{23}
\]

Now suppose \(5/8\le\rho_3<1\). On \(v\in[1/8,1/5]\),
the incoming shifted cosine is less than \(-3/10\), the outgoing
shifted cosine is less than \(-1/2\), and the own cosine is greater
than \(3/10\). The own square is at most
\[
                         D_s=1+\rho^2-\frac35\rho.
 \tag{24}
\]
The outgoing numerator square exceeds
\(1+\rho^2/4+\rho/2>D_s\). The incoming square exceeds
\(225/256+\rho^2+9\rho/16>D_s^2\): indeed
\(D_s\le1+2\rho/5\), and
\[
 \frac{21}{25}\rho^2-\frac{19}{80}\rho-\frac{31}{256}
 \ge\frac{15}{256}\qquad(\rho\ge5/8),
 \tag{25}
\]
since this quadratic is increasing there. Thus every second maximizer
has \(v\ge1/5\). Now \(q+v\ge.65\), \(\rho_3^{-1}\le8/5\), and
\(\sin(\pi/5)<3/5\), so
\[
                         N_3^2\le
 B_l:=r^2+\frac{48}{25}r+\frac{64}{25}.
 \tag{26}
\]
The last sine bound follows from
\(\sin(\pi/5)=\sqrt{10-2\sqrt5}/4\) and \(\sqrt5>53/25\).

## 5. Maximum transport and the original reserve

Put \(D_q=|1-re^{-2\pi iq}|\). Since
\(\cos(\pi/10)>19/20\), using \(\pi^2<10\),
\[
                   D_q^2\ge D_0:=r^2+\frac{19}{10}r+1.
 \tag{27}
\]
At a pair of maximizing indices, direct differentiation of (3) gives
the forced alternative's \(q\)-partial derivative
\[
                         \log\frac{N_2N_3}{D_q^2}.
 \tag{28}
\]
For the factorial alternative subtract \(\log D_q>0\).
The forcing denominator is \(D_q^2\), not \(D_q^3\).

In the large-\(\rho_3\) range (28) is negative, because
\[
 D_0^2-A_fB_l
 =\frac{251}{200}r^3+\frac{17}{20}r^2
             +\frac7{25}r-\frac{39}{25}>0\qquad(r\ge1).
 \tag{29}
\]
Its value at one is \(33/40\); the other coefficients are positive.
For the small-\(\rho_3\) range,
\[
 \begin{split}
 {\cal P}(r)&=\frac{81}{80}D_0^2-A_fB_s\\
 &=\frac1{80}r^4+\frac{3633}{2000}r^3
       +\frac{1531}{8000}r^2+\frac{741}{4000}r
       -\frac{1039}{400}.
 \end{split}
 \tag{30}
\]
This is increasing for \(r>0\), and
\[
 {\cal P}(17/16)=\frac{5309604}{524288000}>\frac1{100}.
 \tag{31}
\]
Also \(D_0<21/5\), since \(D_0(16/15)=937/225<21/5\);
therefore \(D_0^2<18\). Consequently
\[
 \left(\frac{N_2N_3}{D_q^2}\right)^2
 <\frac{81}{80}-\frac1{1800}=1+\frac{43}{3600},
 \qquad
 \log\frac{N_2N_3}{D_q^2}<\frac{43}{7200}.
 \tag{32}
\]

Maximizers need not be unique or differentiable. Both maxima in (3)
are over fixed compact intervals of functions with bounded first
derivatives, so they are Lipschitz. Their upper right derivatives are
bounded by the largest \(q\)-partial derivative at a maximizer:
choose maximizers at \(q+h\), pass to a convergent subsequence as
\(h\downarrow0\), and subtract their value at \(q\). The limiting
point maximizes at \(q\). Apply this to the single maximum over the
product of both private intervals. The barriers above imply the
almost-everywhere derivative bound (32) for either allocated maximum.
Integration over a length at most \(1/20\), starting from (6), leaves
\[
 \frac1{3200}-\frac1{20}\frac{43}{7200}
       =\frac{45-43}{144000}=\frac1{72000}.
 \tag{33}
\]
This proves (7), including maximizer switches and degeneracies.

## 6. Cap attachment and finite-source scope

Let \(L_1\) be the original allocated cap action, with bare phase
\(\Psi(e,a)\) and allocated phase \(\Xi_1(e,a)=\Psi(e,a)-g(a)/2\).
Retain each original cap profile \(A_i(a)\), including the main,
real cuts, both aliases and their joins, and the true-end profiles.
The [complete cap plane](research_mixed_first_cap_plateau_completion.md)
and its profilewise use in
[the negative first-left connection](research_mixed_complete44_second_selected_negative_left_connection.md),
Section 1, give
\[
 A_i(a)-\tfrac12\Re g(a)
 \le \Re\{L_1(a_*)+L_1'(a_*)(a-a_*)\}
                  -\kappa(x-\Re a_*)^2,
 \quad\kappa=1/2500000.
 \tag{34}
\]
The original critical equation \(L_1'(a_*)+p_L=0\) therefore yields,
with the unchanged affine action
\[
 \Lambda_{123}(z)=
 \Re\{L_1(a_*)+F_{23,*}+p_R(z-z_*)\},
 \tag{35}
\]
the bound
\[
 A_i(a)+M_2(q)+M_3(q)-\Re g(a)
          +W^\nu(y)-\tfrac12\Re g(z)
 \le\Lambda_{123}(z)-\frac1{72000}
                    -\kappa(x-\Re a_*)^2.
 \tag{36}
\]
It retains the literal allocation of
\[
 U_{1,N}(w,X)\,C_{1,N}(X,Y)\,C_{1,N}(Y,Z)\,
          d_N(X)d_N(Y)Y^{-N}\quad\text{with }|d_N(Z)|^{1/2},
 \tag{37}
\]
when both ordinary factors are restricted to their original main
horizontal currents. There is no \(X^{-N}\): the first coordinate
is unselected. The
[Fourier continuation](research_mixed_fourier_weight_continuation.md)
gives the full first-weight rate \(-\Re g(a)\) at its negative
height; its forcing rate is smaller. The full second weight has
exactly the two alternatives (4). The third halfweight remains
\(-\Re g(z)/2\). No finite polynomial is divided out and no finite
cap or kernel lower bound is inferred.

The bound (36) is pointwise in every retained cap profile and both
ordinary main indices before integration. On fixed compact regular
main contours it gives the usual polynomial-prefactor upper bound
with any prescribed positive rate tolerance. The original \(+N\)
main-current factors and both level parities remain unchanged.
The strict margin persists on sufficiently small ordinary-color/source
neighborhoods where the original cap symbols are licensed.
Physical low/high rows, ordinary real cuts, alias horizontals and
vertical joins still require their own complete-source comparison
on this positive shoulder.

## 7. Direct-source bindings

All new scalar comparisons above are written inequalities. No new
mathematical numerical evaluation, saved-value arithmetic, test, import
or compilation was used. The original central deficit is imported as
its stated theorem, without replaying its certificate.

| Direct source | SHA256 | Implication |
|---|---|---|
| [Reference curve](research_mixed_second_selected_reference_curve.md) | 4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5 | Actual coupled family, original lifts, heights and following-leg distinction |
| [Central completion](research_mixed_second_selected_central_completion.md) | ad694fed3707db09dfe1d926affdabf7557d519f142d975e9cc02fe54bf3ce00 | Original allocated phase, marginals, both alternatives and common \(1/3200\) deficit |
| [Cap plateau](research_mixed_first_cap_plateau_completion.md) | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d | All cap profiles and true ends under the original plane |
| [Negative first-left connection](research_mixed_complete44_second_selected_negative_left_connection.md) | 878cbd67c6035f6fb9903e76d0b719cae599874d852710d979282e711d7fbf77 | Exact three-factor allocation and marginal cancellation |
| [Fourier continuation](research_mixed_fourier_weight_continuation.md) | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e | Complete weight alternatives and zero-safe interpretation |

The new result is (7) and its cap attachment (36), not the remaining
finite-source signs or a whole-word theorem.
