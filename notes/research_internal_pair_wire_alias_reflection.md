# A joint reflection estimate for the lower wire alias

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The lower shared-wire contour has an exact Fourier penalty.
For a coupled pair, estimating each reflected Newton factor by a
separate \(2\pi y\) loss is too weak: there are two such factors,
whereas the wire penalty is only \(2\pi y\). On a compact chamber
containing the actual pair saddle, each factor has the sharper
loss strictly less than \(\pi y\). The resulting comparison is
between the actual upper and lower joint densities, with the
same trace paths and all original crossing phases retained.

This proves a lower-alias bound wherever the upper absolute
density has already been controlled in that chamber. It does
not assert that the entire original middle contour lies there,
or replace the still-required upper-contour estimate.

## 1. A reflection identity with its logarithmic branches

Use
\[
 \begin{split}
 b(x,t)&=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),\\
 J'(z)&=\Log(2\sin\pi z),\qquad J(0)=0,\\
 x_\pm&=\xi\pm iy,\qquad t=\tau-ih .
 \end{split}
 \tag{1}
\]
Initially impose fixed compact bounds
\[
 0<\alpha\le\xi\le\beta<1/4,\qquad
 |\tau|\le T<\pi/2,\qquad 0\le h\le H,\qquad 0\le y\le Y.
 \tag{2}
\]
The same assumptions, with its own height bound, will be
used for the second trace angle \(r\). Every shifted factorial
argument in (1) has real part in a fixed compact subinterval
of \((0,1)\), independently of its imaginary part. Thus the
original strip primitive is single-valued throughout the
reflection. No negative-argument reset is made.

Put
\[
 \begin{split}
 D_t(y)&=\Re b(\xi-iy,t)-\Re b(\xi+iy,t),\\
 \cos t&=c+id,\qquad
 R_s=\cos(2\pi\xi)\cosh(2\pi s)+c,\qquad
 B_s=\sin(2\pi\xi)\sinh(2\pi s).
 \end{split}
 \tag{3}
\]
Here \(c=\cos\tau\cosh h>0\); \(d\) can have either sign.

**Lemma 1.** For \(0\le s\le y\),
\[
 D_t'(s)=\arg\{R_s+i(d+B_s)\}
                       +\arg\{R_s+i(d-B_s)\},
 \tag{4}
\]
where both arguments are the principal arguments in
\((-\pi/2,\pi/2)\). In particular \(D_t'(s)<\pi\).

*Proof.* Differentiation of the strip primitive gives
\[
 b_x(x,t)=
   \Log\frac{\cos(2\pi x)+\cos t}{1-\cos(2\pi x)} .
 \tag{5}
\]
The logarithm means its continuation from the original strip.
Differentiating the two terms in \(D_t\) takes the imaginary
part of the sum of their \(b_x\)'s. The two denominator
logarithms in that sum are conjugates; their imaginary parts
cancel. The numerators are exactly the two quantities in (4).
Their real parts \(R_s\) are strictly positive by (2).
At \(s=0\), the argument of the product of the two original
shifted sine factors agrees with the principal argument
of this numerator: each shifted cosine has positive real
part and their product has positive real part.
Continuation through \(R_s>0\) therefore introduces no
multiple of \(2\pi\). This proves (4). Each argument lies
strictly between \(-\pi/2\) and \(\pi/2\), proving the claim.
\(\square\)

The compact bounds give explicit positive constants
\(\rho,L\) such that
\[
 R_s\ge\rho>0,\qquad |d+B_s|,|d-B_s|\le L.
 \tag{6}
\]
For example one may take
\(\rho=\cos(2\pi\beta)+\cos T\) and
\(L=\sinh H+\sinh(2\pi Y)\).
For two trace factors, use the smaller \(\rho\) and larger
\(L\) of their two bounds. Set
\[
                 \gamma=2\pi-4\arctan(L/\rho)>0.
 \tag{7}
\]
Since \(D_t(0)=D_r(0)=0\), (4)–(7) give the joint bound
\[
                         D_t(y)+D_r(y)\le(2\pi-\gamma)y.
 \tag{8}
\]

## 2. The exact Fourier penalty beats this joint loss

The original shared-index Cauchy kernel is
\[
                 \mathcal C_N(x)=\frac1{1-e^{2\pi iNx}} .
 \tag{9}
\]
For every real \(\xi\) and \(y>0\) its moduli obey the exact
identity
\[
              \frac{|\mathcal C_N(\xi-iy)|}
                   {|\mathcal C_N(\xi+iy)|}=e^{-2\pi Ny}.
 \tag{10}
\]
To check it, put \(z=e^{2\pi iN\xi}\) and \(q=e^{-2\pi Ny}\).
Then \(|1-q^{-1}z|=q^{-1}|1-qz|\).

Let \(B_N(x,t)\) be the canonical factorial representative
used inside the original retained trace. In the compact
strip (2), its two-sided uniform expansion is
\[
 B_N(x,t)=\frac{e^{Nb(x,t)}}{2N\sin(\pi x)}
                                      (1+O(N^{-1})).
 \tag{11}
\]
All its factors are nonzero there. This is the original
factorial expansion with its half-integer shifts; it is not
an asymptotic assigned to a formal interpolation.
The amplitudes at \(x_+\) and \(x_-\) have equal moduli because
\(|\sin(\pi x_+)|=|\sin(\pi x_-)|\).

**Theorem 2.** Uniformly on (2), for both level parities,
\[
 \begin{split}
 &|\mathcal C_N(x_-)B_N(x_-,t)B_N(x_-,r)|\\
 &\hspace{15mm}\le
 C e^{-\gamma Ny}
       |\mathcal C_N(x_+)B_N(x_+,t)B_N(x_+,r)|.
 \end{split}
 \tag{12}
\]
For \(y\ge y_0>0\), this is a fixed exponential gap.

*Proof.* Divide the moduli in (11) at the reflected points.
The paired amplitude moduli cancel, leaving
\(e^{N(D_t(y)+D_r(y))}(1+O(N^{-1}))\).
Multiply by the exact ratio (10) and apply (8).
A fixed constant absorbs the uniform remainders. \(\square\)

The rest of the original two-trace density consists of
\[
 K_N(t,u)K_N(r,v)\sin t\sin r\,
 \frac{\exp\{iN(nt^2+pr^2)/(4\pi)-iN(t+r)\}}
 {(1-\eta e^{-iNt})^2(1-\eta e^{-iNr})^2},
 \qquad \eta=(-1)^{N-1}.
 \tag{13}
\]
It is identical at \(x_+\) and \(x_-\). Multiplying (12)
by its modulus proves the same comparison for the full
joint density. This does not require either outside kernel
to be nonzero, and it uses no separate asymptotic for
\(W_{n,N}\) or \(W_{p,N}\).
The crossing phases, all higher trace charges and the first
normals represented by the double poles are unchanged.
Fixed derivatives in the outside colors may likewise be
taken in the common factors before applying the comparison.

## 3. Paired contours and the exact scope of the estimate

The two reflected wire curves may be graphs
\(x_\pm(\xi)=\xi\pm iy(\xi)\). Use the same lower trace paths
at these two points. Such a choice is legitimate by the
[pointwise trace-deformation lemma](research_internal_pair_endpoint_taper.md);
the trace contours may depend smoothly on \(\xi\).
The upper and lower wire tangents have equal absolute
Jacobians, \(|1+iy'|=|1-iy'|\). The trace tangents are the
same on the two pieces. Consequently, for a paired region
on which (2) holds and \(y(\xi)\ge y_0>0\),
\[
 \int_{\rm lower}|\text{original density}|
       \le C e^{-\gamma Ny_0}
                   \int_{\rm upper}|\text{original density}|.
 \tag{14}
\]
The exact orientation of the lower contour has no effect
on this absolute upper bound. In particular, if the upper
absolute integral on this region is at most
\(CN^A e^{NM_{n,p}}\), the lower alias has a strict gap
below the geometric rate.

The comparison in (14) is with the upper **absolute** integral.
It is not a lower bound on the signed upper integral, and
cannot exclude cancellation in a region where that absolute
integral has not been controlled.

Every fixed positive pair saddle lies in (2) for suitable
strict cuts: its wire has \(0<\Re x_*<1/4\), and its two
angles have \(0<\Re t_*,\Re r_*<\pi/2\).
Thus a full neighborhood of the coupled local Gaussian has
an exponentially smaller reflected alias. The
[explicit local packet](research_internal_pair_local_gaussian.md#7-the-explicit-local-packet-with-two-free-outside-colors)
bounds its upper absolute density and supplies its nonzero
local coefficient. This deduction holds without an
independent one-vertex geometric packet.

More generally the proof applies on any compact domain where
the original shifted factorial real parts remain in \((0,1)\)
and, for both trace angles and every intermediate reflection
height,
\[
          \cos(2\pi\xi)\cosh(2\pi s)+\Re\cos t>0.
 \tag{15}
\]
A positive lower bound in (15) replaces the explicit \(\rho\)
in (6). The simple chamber (2) guarantees it automatically.

Outside this domain a numerator can enter the left half-plane.
The separate argument bounds used in (4) then no longer give
a combined loss smaller than \(2\pi y\). Reflected factorial
identities may also introduce additional terms or moving
poles if their factors are separated. None of those terms
has been discarded here. Extending the paired-contour bound
through the remaining middle region, together with the
upper principal estimate there, remains necessary for a
general full-source theorem.


## 4. Extension through the regular chamber beyond \(\Re x=1/4\)

The positive-real-part condition (15) is sufficient but is not
necessary. The argument can be continued when \(R_s\) turns
negative, provided that it does so on the correct side of
the moving numerator.

**Proposition 3.** Let the parameters range over a fixed compact
subset of
\[
 0<\xi<1/2,\qquad |\tau|<\pi/2,\qquad
       \xi+\frac{|\tau|}{2\pi}<\frac12,\qquad h\ge0,\quad y\ge0.
 \tag{16}
\]
Then the derivative in (4), with its original continuation,
satisfies
\[
                              -\pi<D_t'(s)<\pi
                          \qquad(0\le s\le y).
 \tag{17}
\]
For two trace factors in this chamber, the joint density
comparison (12) therefore holds with some uniform
\(\gamma_{\rm reg}>0\), even when the interval of wire real
parts extends past \(1/4\).

*Proof.* By conjugation it is enough to consider \(\tau\ge0\),
so \(d=\sin\tau\,\sinh h\ge0\). Put
\[
 q=\cos(2\pi\xi),\qquad c_\tau=\cos\tau .
 \tag{18}
\]
If \(q\ge0\), then \(R_s=q\cosh(2\pi s)+c_\tau\cosh h>0\),
and Lemma 1 applies directly.

Suppose \(q<0\). The strict factorial inequality in (16)
gives \(c_\tau>-q>0\). Thus \(R_0>0\), and \(R_s\) decreases
with \(s\), whereas \(B_s\) increases. At any zero of \(R_s\),
direct substitution gives
\[
 B_s^2-d^2
    =(c_\tau^2-q^2)
                  \left(\frac{\cosh^2h}{q^2}-1\right)>0.
 \tag{19}
\]
Consequently \(B_s>d\) before \(R_s\) can turn negative.
The numerator \(R_s+i(d-B_s)\) crosses the real axis while
its real part is positive. It then enters the lower half-plane
with its principal argument; it acquires no extra winding.
The other numerator stays in the upper half-plane.

While \(R_s>0\), the sum of the arguments belongs to
\([0,\pi)\). When \(R_s<0\), it instead equals
\[
 \arctan\frac{B_s-d}{-R_s}
               -\arctan\frac{B_s+d}{-R_s}\ \in(-\pi/2,0].
 \tag{20}
\]
At \(R_s=0\) the two arguments sum to zero. These formulas
prove (17) for nonnegative \(\tau\), including \(d=0\) by
continuity. Replacing \(\tau\) by \(-\tau\) conjugates and
exchanges the two numerators, so it changes the sign of
their argument sum. This proves (17) in general.

No numerator vanishes: all the original shifted factorial
real parts lie strictly between zero and one. The derivative
is therefore continuous on each compact parameter set in
(16), including the intermediate reflection heights.
Its upper bound is uniformly strictly below \(\pi\).
For two factors their sum is uniformly below \(2\pi\).
Integrate from \(s=0\), apply the exact wire ratio (10), and
repeat the two-sided factorial argument in Theorem 2.
This proves the claimed uniform joint density comparison.
\(\square\)

Thus the lower alias is controlled throughout the part of
the original positive factorial chamber with both trace
real parts strictly between \(-\pi/2\) and \(\pi/2\).
This is compatible with the existing mixed concavity domain
and does not require an individual one-vertex saddle theorem.
Regions with larger trace real parts or beyond a factorial
wall remain outside this proposition. Their original currents
and wall residues still require a coupled argument.
