# The complete conditional packet on the real incoming arc

Research deduction, 7 November 2026. The whole original conditional
polynomial has a nonzero asymptotic expansion for every real incoming
coordinate \(1/2\le a\le7/10\), uniformly over the selected outgoing
rectangle. This statement retains every physical row, including rows
past the numerator wall, both parities, all four residue sides, and
both unweighted main-path connectors.

The new inputs are a uniform critical-point chart, all-height
horizontal concavity, and an own-action lower bound. They allow the
existing exact finite-source decomposition to be calibrated to this
conditional action itself. No complete-cap continuation, selected
affine comparison, whole later Fourier sector, or knot-family
conclusion is inferred. No numerical evaluation is used.

## 1. Source, original sheet, and exact phase

Keep
\[
\begin{gathered}
r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                  \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
\mathcal A=[1/2,7/10],\qquad
\mathcal Y=\{11/50\le\Re y\le9/20,\quad0\le\Im y\le1/100\},\\
X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy}.
\end{gathered}                                                    \tag{1}
\]
The primitive and phase are the original ones:
\[
\begin{split}
g'(z)&=\Log(1-e^{-2\pi iz}),\qquad
g''(z)=\pi(\cot\pi z-i),\quad0<\Re z<1,\\
Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat .
\end{split}                                                       \tag{2}
\]
The logarithm in the first line is principal on this strip.
No additive constant in \(g\) is changed.

The [general incoming transport theorem, Section 3](research_mixed_half_face_general_incoming_transport.md)
proves that
\[
(1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0                                  \tag{3}
\]
has exactly one upper-half-plane root \(v=v(a,y)\), counting
multiplicity, on \(\mathcal A\times\mathcal Y\). It is simple, and
\[
t(a,y)=\frac{\Log v(a,y)}{2\pi i},\qquad
0<\Re t<1-a,\qquad Q_t(t(a,y);a,y)=0.                            \tag{4}
\]
Here \(\arg v\in(0,\pi)\), and the last equality has the original
zero logarithmic lift. Every phase argument in (2) is regular.
The same theorem supplies a holomorphic continuation to a fixed
complex neighborhood of this compact parameter set. The
[global phase-decrease theorem, Lemma 1](research_mixed_half_face_global_phase_decrease.md)
proves the sharper bound \(|v|<2\) there on the real base set.
We use that bound, but do not use a finite-source conclusion from
either phase theorem.

Write
\[
          \Theta(a,y)=Q(t(a,y);a,y),\qquad
                         M(a,y)=\Re\Theta(a,y).                 \tag{5}
\]

## 2. A uniform critical-point chart

**Lemma 1.** On \(\mathcal A\times\mathcal Y\),
\[
 \frac12<|v|<2,\qquad
 \frac1{16}<\Re t<1-a,\qquad
       |\Im t|<\frac{\log2}{2\pi}<\frac3{25}.                    \tag{6}
\]
All real-part distances in (6) have positive uniform minima on
the compact base set.

*Proof.* Only the lower radius and lower real-part bounds are new.
Suppose first that \(\rho=|v|\le1/2\), and put
\(\phi=\arg v\), \(\theta=\arg X=2\pi(1-a)\), \(x=\Re y\).
The original strips give \(0<\phi<\theta\le\pi\). Rewriting the
original logarithms on these strips gives exactly
\[
 Q_t=\Log v+\Log Y-i\pi+
       \Log(1-v/X)+\Log(1-v/Y)-3\Log(1-v).                       \tag{7}
\]
For example the incoming logarithm is
\(\Log(1-v/X)+\Log X-\Log v-i\pi\); the outgoing one is
\(\Log(1-v/Y)+\Log Y-\Log v+i\pi\). Their combination with
the own denominator and \(2\pi ia\) yields (7).
These identities can also be checked first as \(\rho\downarrow0\)
inside the stated strips and continued without crossing a divisor.
The three small-disk logarithms in (7) are principal.

Let \(A_\rho(\phi)=\arg(1-\rho e^{-i\phi})\) for \(0\le\phi\le\pi\).
Then
\[
 \frac{d}{d\phi}\{\phi+3A_\rho(\phi)\}
     =\frac{1+\rho\cos\phi-2\rho^2}
                  {1-2\rho\cos\phi+\rho^2}\ge0
                  \qquad(0<\rho\le1/2).                        \tag{8}
\]
Its value at \(\phi=\pi\) is \(\pi\). The two remaining logarithms
in (7) have arguments of modulus at most \(\arcsin(1/2)=\pi/6\),
since \(|X|=1\) and \(|Y|\ge1\). Consequently
\[
       \Im Q_t\le -2\pi x+\frac{\pi}{3}
                    \le-\frac{8\pi}{75}<0,
\]
contradicting (4). Thus \(|v|>1/2\). Together with the imported
upper bound, this proves the height estimate in (6).

Now suppose \(u=\Re t\le1/16\), and set \(R=e^{2\pi\Im t}\).
The radius bounds just proved give \(1/2<R<2\). Put
\[
\begin{split}
D&=|1-Re^{-2\pi iu}|^2,\\
A&=|1-Re^{-2\pi i(a+u)}|^2,\\
B&=|1-Re^{2\pi\Im y-2\pi i(x+u)}|^2 .
\end{split}
\]
Elementary angle bounds give
\[
\cos2\pi u>9/10,\quad
\cos2\pi(a+u)<1/12,\quad
\cos2\pi(x+u)<1/5.                                               \tag{9}
\]
Indeed \(a+u\le61/80\), so its cosine is at most
\(\sin(\pi/40)<1/12\); the outgoing cosine is at most
\(\sin(3\pi/50)<1/5\). The own cosine bound follows from
\(\cos(\pi/8)>9/10\). In the outgoing factor the radius can
only increase its modulus, because \(R>1/2>\cos2\pi(x+u)\).
It follows that
\[
\begin{split}
D&<D_0:=1+R^2-\tfrac95R\le7/5,\\
A&>1+R^2-R/6>2D_0,\qquad
B>1+R^2-\tfrac25R>2D_0 .                                       \tag{10}
\end{split}
\]
For the last two comparisons, the differences from \(2D_0\)
are respectively \(-1-R^2+103R/30\) and
\(-1-R^2+16R/5\). They are positive at both endpoints
\(R=1/2,2\), hence throughout the interval by concavity.
The exact exponentiated equation (2) has squared modulus
\(AB/D^3>4/D>20/7>1\), again a contradiction.
Thus \(\Re t>1/16\). Compactness and continuity supply the
claimed strict uniform distances. \(\square\)

## 3. All-height horizontal concavity

Write \(C(z)=\Re\cot\pi z\). Its exact formula is
\[
 C(u+ih)=\frac{\sin2\pi u}
                         {\cosh2\pi h-\cos2\pi u}.               \tag{11}
\]

**Lemma 2.** For every real \(h\), every \(a,y\) in the base set,
and
\[
                         3/50\le u<1-a,
\]
one has
\[
                   \Re Q_{tt}(u+ih;a,y)<0.                     \tag{12}
\]
On any compact subset with bounded height and a fixed distance
from the incoming numerator wall, this inequality has a uniform
strict reserve.

*Proof.* The real part of \(a+t\) lies in \((1/2,1)\), so
\(C(a+t)<0\), while \(C(t)>0\). If \(u+x\ge1/2\), then
\(C(t+y)\le0\), and (12) follows at once.

Otherwise \(u+x<1/2\), but \(u+x\ge7/25>1/4\).
Writing \(H=\Im y\), the correlated height inequality
\(\cosh2\pi(h+H)\ge e^{-2\pi H}\cosh2\pi h\), together with
\(\cos2\pi(u+x)<0\), gives
\[
\frac{C(t+y)}{C(t)}
\le e^{2\pi H}
\frac{\sin2\pi(u+x)}{\sin2\pi u}
\frac{\cosh2\pi h-\cos2\pi u}
     {\cosh2\pi h-\cos2\pi(u+x)}
<\frac{e^{\pi/50}}{\sin2\pi u}.                                 \tag{13}
\]
Here \(\cos2\pi u>\cos2\pi(u+x)\).
Since \(3/50\le u<7/25\),
\[
\sin2\pi u>\sin(3/8)\ge\frac38-\frac{(3/8)^3}{6}
                  =\frac{375}{1024}.
\]
The original elementary radius bound \(e^{\pi/50}<175/164\)
therefore makes the last ratio in (13) smaller than
\[
                         \frac{1792}{615}<3.                    \tag{14}
\]
Thus \(C(a+t)+C(t+y)-3C(t)<0\), proving (12).
The final assertion follows by compactness. \(\square\)

The phase on the horizontal line through \(t(a,y)\) has its
unique maximum at that point. The real phase along every
vertical segment in the retained strip is strictly convex.
This lemma applies to either sign of the critical height.

## 4. A uniform own-action floor

**Lemma 3.** Uniformly on the base set,
\[
                              M(a,y)>13/24.                    \tag{15}
\]

*Proof.* We use the real trial \(t_0=1/5\). First, with
\(c=-J(1/4)\), the alternating Catalan series gives
\[
c>\frac{29}{200}.
\]
Here is a finite rational witness. Its first six alternating
terms exceed
\[
 \frac89+\frac{19}{1000}+\frac4{1000}
       =\frac{8207}{9000}>\frac{319}{350};
\]
the two differences used are
\(1/25-1/49>19/1000\) and \(1/81-1/121>4/1000\).
Multiplication by \(1/(2\pi)>7/44\) proves the stated bound.
Also \(2\sin(\pi/5)>7/6\), because
\(\sin(\pi/5)>\sin(5/8)\ge1795/3072>7/12\).
Since \(\log(7/6)>2/13\),
\[
              -J(1/5)>c+\frac1{20}\log(7/6)
                         >\frac{29}{200}+\frac1{130}
                         =\frac{397}{2600}.                    \tag{16}
\]

The real outgoing contribution at \(t_0\) is
\[
 I_y=\int_0^{1/5}
       \log|1-e^{2\pi H-2\pi i(x+s)}|\,ds .
\]
Increasing \(H\ge0\) increases every modulus, so it suffices to
bound the radius-one integral. That integral is a concave
function of \(x\) on \([11/50,9/20]\); hence its minimum is at
an endpoint. The trapezoid lower bound for the concave function
\(\log(2\sin\pi s)\) gives
\[
 I_y\ge\frac1{10}
       \log\{4\sin\pi x\,\sin\pi(x+1/5)\}
                         >\frac1{10}\log(19/8)>\frac{17}{200}.
                                                                    \tag{17}
\]
At the left endpoint the two sines exceed \(5/8,19/20\);
at the right endpoint they exceed \(19/20,4/5\).
The \(19/20\) bounds follow from
\(\cos(2\pi/25)>19/20\), using \(1-z^2/2\) as a lower
bound for \(\cos z\). For the final logarithm inequality,
\[
 \log(19/8)>
 2\left(\frac{11}{27}+\frac{(11/27)^3}{3}\right)
 =\frac{50776}{59049}>\frac{17}{20};
\]
the final cross-product difference is \(11687>0\).

The incoming real contribution
\[
                         I_a=J(a+1/5)-J(a)
\]
decreases with \(a\in[1/2,7/10]\).
For \(a\ge3/5\), subdivision of \([7/10,9/10]\) at \(4/5\)
and the two trapezoid lower bounds give
\[
 I_a\ge I_{7/10}>\frac1{10}\log(2\sin(\pi/5))>\frac1{65}.
                                                                    \tag{18}
\]
The outer endpoint logarithms sum to zero because
\(4\sin(3\pi/10)\sin(\pi/10)=1\).
For \(a\le3/5\), a single trapezoid bound on \([3/5,4/5]\)
instead gives
\[
 I_a\ge I_{3/5}>
 \frac1{10}\log(133/60)>\frac3{40}.                              \tag{19}
\]
Indeed \(\sin(2\pi/5)>19/20\), \(\sin(\pi/5)>7/12\),
and \(\log(133/60)>146/193>3/4\).
The sine bound follows, for example, from
\(\sin^2(2\pi/5)=(5+\sqrt5)/8>361/400\).

It remains to control the change to the actual critical height
\(h_*=\Im t(a,y)\). By Lemma 1,
\(|h_*|<\log2/(2\pi)\). Throughout this vertical interval at
\(t_0=1/5\), (11) gives \(C(t_0+ih)>1\), because
\[
\cosh2\pi h\le5/4,\quad
\sin(2\pi/5)>19/20,\quad\cos(2\pi/5)>3/10.
\]
The outgoing cotangent is at most
\(\cot(21\pi/50)=\tan(2\pi/25)<1/3\); when its real part
passes \(1/2\), it is nonpositive. This tangent inequality
follows from \(\sin z<z\), \(\cos z>1-z^2/2\) and
\(2\pi/25<4/15\).
The incoming cotangent is always negative. If \(a\ge3/5\),
it is less than \(-1\): for \(a+t_0\in[4/5,9/10]\),
\[
 |\sin2\pi(a+t_0)|+\cos2\pi(a+t_0)>5/4.
\]
The sum is concave after reflection to
\([\pi/5,2\pi/5]\), and both endpoint values exceed \(5/4\)
by the elementary sine and cosine bounds just used.
Consequently the vertical second derivative satisfies
\[
 \partial_h^2\Re Q(t_0+ih;a,y)>
 \begin{cases}
   8\pi/3,&1/2\le a\le3/5,\\
   11\pi/3,&3/5\le a\le7/10.
 \end{cases}                                                    \tag{20}
\]

At \(H=0,h=0\), the imaginary derivative is exactly
\(\pi(a-3/10-x)\). Only the outgoing logarithm changes when
\(0\le H\le1/100\). Since \(x+t_0\in[21/50,13/20]\)
has nonpositive doubled-angle cosine, its argument changes by
at most half the change in logarithmic radius, hence by at most
\(\pi/100\). Thus
\[
 |\Im Q_t(t_0;a,y)|\le
 \begin{cases}
   26\pi/100,&a\le3/5,\\
   19\pi/100,&a\ge3/5.
 \end{cases}                                                    \tag{21}
\]
If a real function has second derivative at least \(K>0\)
on the interval joining zero to \(h_*\), its value at \(h_*\)
is at least its value at zero minus its initial derivative
squared divided by \(2K\). Equations (20)--(21) therefore bound
the vertical loss by
\[
 \begin{cases}
   507\pi/40000<1/25,&a\le3/5,\\
   1083\pi/220000<1083/70000,&a\ge3/5.
 \end{cases}                                                    \tag{22}
\]
The first comparison uses \(11154<11200\); both use
\(\pi<22/7\).

The trial real phase from (16)--(19) is larger than
\(1607/2600\) in the first case and \(363/650\) in the second.
After (22), both exceed \(13/24\):
\[
 \frac{1607}{2600}-\frac1{25}>\frac{13}{24},\qquad
 \frac{363}{650}-\frac{1083}{70000}>\frac{13}{24}.                 \tag{23}
\]
For the latter, \(363/650-13/24=131/7800\), and the
cross-product difference against \(1083/70000\) is \(722600\).
Finally \(t_0<1-a\), and Lemma 2 makes the actual horizontal
critical point the maximum on its height line. Its value is
at least this translated trial value. This proves (15).
\(\square\)

## 5. The whole finite source and every remaining current

Use the zero-safe physical row bounds of
[the end-range theorem, Sections 1--3](research_mixed_next_selected_first_wall_rows.md).
They apply to the larger real incoming interval
\([1/2,13/16]\), hence to \(\mathcal A\). With periodic \(J\), put
\[
 F_a(s)=L(s)+J(a+s)-J(a)-3J(s),\qquad
                         L(s)=-2J((1-s)/2).                    \tag{24}
\]
The complete physical row has unit-\(Y\)-disk rate
\(F_a(j/N)\), up to a polynomial prefactor and any fixed
positive tolerance. This includes all zeros and the true
indices \(0,N-1\). The cited theorem proves
\[
\begin{array}{ll}
 F_a(s)<7/15+1/100,&s\ge1-a-2\varepsilon,\\
 F_a(s)<77/160+1/100,&0\le s\le1/16+\varepsilon_-,
\end{array}                                                      \tag{25}
\]
for fixed positive collars, which may be decreased.

By Lemma 1, choose \(\varepsilon<1/64\) also smaller than
one quarter of the uniform distance \(1-a-\Re t(a,y)\).
Use
\[
\begin{gathered}
L_N=\lfloor N/16\rfloor+1,\qquad
K_N(a)=\lceil N(1-a-\varepsilon)\rceil,\\
\ell_N=(L_N-1/2)/N,\qquad u_N(a)=(K_N(a)-1/2)/N .
\end{gathered}                                                    \tag{26}
\]
For all large \(N\), these cuts lie in
\([3/50,1-a)\), have a fixed positive distance from the critical
point, and belong to the paid collars (25).

For \(|Y|=e^{2\pi H}\ge1\), the degree-\(j\) numerator costs
at most \(2\pi Hj\). The two omitted physical sums and the
corresponding real cuts consequently have the factor-free rates
\[
 E_+=\frac7{15}+\frac1{100}+\frac{\pi}{50}
                <\frac{13}{24}-\frac3{1400},\qquad
 E_-=\frac{77}{160}+\frac1{100}+\frac{\pi}{400}<\frac12 .
                                                                    \tag{27}
\]
The lower collar can be chosen below \(1/8\).
For continuous real cuts the same radius allowance follows
from the centered-arc integral bound, not from interpolation
of physical polynomial degrees; see the end-range theorem,
equation (21). Thus (27) applies to the actual cuts as well
as to the physical sums. Lemma 3 pays them below \(M(a,y)\).

For the retained rows the exact canonical interpolation is
\[
 T_N(t;a,y)=e^{2\pi iNat}\Pi_N(a+t)\Pi_N(y+t)
                          E_N(a)E_N(y)E_N(t)^3.                 \tag{28}
\]
At \(t=j/N\) it is exactly the summand in (1). All its factors
stay in their original regular strips on
\[
               \ell_N\le\Re t\le u_N(a),\qquad|\Im t|\le2.       \tag{29}
\]
In particular the incoming numerator has a fixed real-part
distance from its wall. The exact split residue identity of
[the far-half alias theorem, equation (14)](research_mixed_next_far_half_conditional_aliases.md)
is
\[
\begin{split}
\sum_{j=L_N}^{K_N(a)-1}T_N(j/N;a,y)
 &=N\int_{\ell_N}^{u_N(a)}T_N(t;a,y)\,dt+\mathcal R_N(a,y),\\
\mathcal R_N&=\frac{N}{2i}\left\{
 \int_{\partial\mathcal R^+}T_N(t)[\cot(\pi Nt)+i]\,dt+
 \int_{\partial\mathcal R^-}T_N(t)[\cot(\pi Nt)-i]\,dt
 \right\}.
\end{split}                                                       \tag{30}
\]
The outer boundary is positively oriented. Each sign-half
includes both corresponding vertical sides and its horizontal
side; neither includes a real segment. The zero-mode density
is \(+N\), and no scalar has been removed.

The argument estimates of that theorem apply uniformly to
every \(0\le H\le1/100\). Their upper-height input in the
lower half is only \(e^{2\pi(h+H)}\le e^{\pi/50}\).
They give throughout (29)
\[
 \Re Q(u+ih)-\Re Q(u)\le
 \begin{cases}
   (9\pi/5)h,&h\ge0,\\
   (15\pi/8)|h|,&h\le0 .
 \end{cases}                                                     \tag{31}
\]
On the half-grid vertical sides, the exact remainder kernels
are at most \(2e^{-2\pi N|h|}\). Both full vertical aliases
are therefore bounded by their real cut values with extra
rates \(-\pi h/5\) above and \(-\pi|h|/8\) below.
Equation (27) pays the entire sides up to height two.

For the two horizontal aliases, the same factor-free proof
gives \(F_a(u)<6/5\): use
\(L(u)\le u\log2\), \(J(a+u)-J(a)\le u\log2\),
and \(-J(u)<1/6\). Their radius cost is at most \(\pi/100\)
because \(u<1/2\). At height two the smaller alias loss is
\(\pi/4\), leaving
\[
              \frac65+\frac{\pi}{100}-\frac\pi4
                   <\frac{12}{25}<\frac{13}{24}.                 \tag{32}
\]
This estimate is for the conditional source itself, before
any cap or subsequent conditional/Fourier factor is inserted.

Move the zero-mode segment in (30) to height
\(h_*=\Im t(a,y)\), retaining the two unweighted vertical
connecting segments. By Lemma 2 and compactness, there is
\(\kappa>0\) on the relevant bounded strips such that the
translated cut values satisfy
\[
 \Re Q(u+ih_*;a,y)
       \le M(a,y)-\frac{\kappa}{2}(u-\Re t(a,y))^2,
                           \quad u=\ell_N,u_N(a).               \tag{33}
\]
Both squared distances have a uniform positive lower bound.
Their real ends satisfy (27). Vertical convexity from Lemma 2
bounds each entire connector by the larger of these two
endpoint rates. Thus both unweighted joins are also paid
strictly below \(M(a,y)\), for either sign of \(h_*\).

The zero-safe row estimates, regular-strip factorial estimates,
and compactness now give constants \(C,B,\eta>0\) such that
the sum of every piece just removed or retained as a remainder
is bounded by
\[
                         CN^B e^{N(M(a,y)-\eta)}.               \tag{34}
\]
All tolerances are chosen inside the displayed strict reserves
after fixing the collars and critical-point distances.
This statement includes every physical row past \(a+j/N=1\);
no nonphysical numerator zero is assumed.

## 6. Complete packet and parameter persistence

Let the original factorial symbol be
\[
\begin{gathered}
a_0(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2},\\
b(t;a,y)=
\frac{a_0(a+t)a_0(y+t)}
     {a_0(t)^3a_0(a)a_0(y)},\qquad
\mathcal B(a,y)=
\frac{\sqrt{2\pi}\,b(t(a,y);a,y)}
     {\sqrt{-Q_{tt}(t(a,y);a,y)}} .
\end{gathered}                                                    \tag{35}
\]
These are exactly the \(\beta=1\) symbols of
[the original local source, equation (16)](research_mixed_three_four_next_local_source.md).
Their branches continue from the positive real sine chamber;
the Gaussian square root has positive real part on the base
set by Lemma 2. Every factor is nonzero.

**Theorem.** There is a fixed open neighborhood \(\mathcal V\)
of \(\mathcal A\times\mathcal Y\) on which the whole original
conditional polynomial satisfies
\[
\boxed{\quad
C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})
 =N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
             \bigl(1+O_{\rm hol}(N^{-1})\bigr),\qquad
                              \mathcal B(a,y)\ne0 .
\quad}                                                          \tag{36}
\]
All fixed mixed \(a,y\)-derivatives of the normalized relative
error are \(O(N^{-1})\) on smaller neighborhoods. Both level
parities are included.

*Proof.* On the translated main path,
\[
 T_N(t;a,y)=N^{-3/2}b(t;a,y)e^{NQ(t;a,y)}
                              (1+O_{\rm hol}(N^{-1})).
\]
The unique horizontal maximum and nonzero Hessian give the
oriented Gaussian coefficient (35). Row \(N^{-3/2}\), residue
density \(N\), and Gaussian width \(N^{-1/2}\) give exactly
\(N^{-1}\). The complete error (34) is exponentially smaller.
There is no \(\kappa_N\) or Fourier weight in this source.

For holomorphic persistence, fix a base \((a_0,y_0)\) and keep
the two cuts \(L_N,K_N(a_0)\), all row groups, and the bounded
auxiliary contours fixed on a sufficiently small parameter
neighborhood. The real cut collars and all regular-strip
distances have fixed positive margins, independent of \(N\).
The exact full physical row has zero-safe rate
\[
\begin{split}
R(a,y;s)={}&-2\pi s\Im a-3J(s)\\
&+\int_0^s\log|1-e^{-2\pi i(a+v)}|\,dv
 +\int_0^s\log|1-e^{-2\pi i(y+v)}|\,dv .
\end{split}                                                       \tag{37}
\]
The chirp sign is retained. The uniform continuity and
zero-safe \(O(\log N)\) upper Riemann-sum error for (37) are
proved directly in
[the joint-source theorem, Section 2](research_mixed_half_face_joint_source_packet.md).
They apply on arbitrary bounded parameter neighborhoods of
this compact real base set. Thus all physical end gaps persist
without deleting revived numerator rows.
The bounded weighted contours and the unweighted joins retain
their gaps by ordinary continuity. Move only a small central
part through the continued simple saddle; its short connectors
stay in an already gapped outer portion. Compactness supplies
a fixed neighborhood \(\mathcal V\). The original simple
critical sheet and symbols agree on overlaps. Cauchy's formula
gives the fixed mixed derivative estimates. No derivative of
the stepwise cut \(K_N(a)\) is taken. \(\square\)

This continues the **complete conditional factor** along the
whole real arc, with its original phase and cycle coefficient.
It does not supply the still separate continuation of the
whole first cap or compare their product with the actual
ordinary-next affine action. Those obligations are not replaced
by the critical-action decrease or by this conditional packet.
